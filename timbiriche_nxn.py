import numpy as np

# PREPARANDO LOS DATOS
coorMov = []
cadSoltion = []
yy = []
m = []

nXn= 6   ######********************* MOVER  ************************######
numCuadros = (nXn-1)*(nXn-1) 
constante = 120
                #numero de lineas para 3      24
                #numero de lineas para 4      48
                #numero de lineas para 5      80 
                #numero de lineas para 6      120 
n = nXn
longitud = nXn*nXn
mn = longitud

for x in range(0,longitud):
	cadSoltion.append(0)
yy = cadSoltion	
for x in range(0,longitud):
	m.append(yy)

cadSoltion = []
y = []
busqueda = []
for x in range(0,nXn):
	cadSoltion.append(0)
y = cadSoltion	
for x in range(0,nXn):
	busqueda.append(y)

#llenando unos en movimientos posibles en la cadena "m"

def movimientosPosibles(xDefi):
	movimientos = []
	##        ORILLAS EN EL TIMBIRICHE
	# extremo inferior
	if xDefi == 1: 
		movimientos = [2,1+n]
	if xDefi == n: 
		movimientos = [n-1,n+n]
	# extremo superior
	if xDefi == (mn-n+1): 
		movimientos = [(mn-n+1)-n,(mn-n+1)+1]
	if xDefi == mn: 
		movimientos = [mn-n,mn-1]
	if  xDefi < n and xDefi>1:
		movimientos = [xDefi-1,xDefi+1,xDefi+n]
	if  xDefi > (mn-n+1) and xDefi<mn:
		movimientos = [xDefi-n,xDefi-1,xDefi+1]
	for xD in range(1,n-2+1):
		if xDefi == n*xD + 1: 
			movimientos = [xDefi-n,xDefi+1,xDefi+n]
	for xD in range(2,n-2+2):
		if xDefi == n*xD: 
			movimientos = [xDefi-n,xDefi-1,xDefi+n]
	cont3for = 0
	for xD in range(0,(n-2)*(n-2)):
		if xDefi == n+2+cont3for: 
			movimientos = [xDefi-n,xDefi-1,xDefi+1,xDefi+n]
		if ((xD+1)%(n-2)) == 0:
			cont3for = cont3for + 2	
		cont3for = cont3for + 1

	return movimientos

matrizMov = []
OPERADORES1 = [];
for xDef in range(0,longitud):   # nos da la posicion en la que vamos del arreglo de nXn
	resultF = movimientosPosibles(xDef+1)
	i = 0			######********************* MOVER  ************************######
	apendice = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	
	#cadena para 3      [0,0,0,0,0,0,0,0,0] 
	#cadena para 4      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#cadena para 5      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#cadena para 6      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	##### print(resultF)
	OPERADORES1.append(resultF)
	if len(resultF) != 0: # esta linea se puede borrar cuando se acaben los casos de llenado 2,3 y 4
		for y in range(0,longitud):   # revisa en que posicion poner un uno
			if resultF[i] == y+1:
				apendice[y] = 1
				i = i + 1
			if i >= len(resultF):
				matrizMov.append(apendice)
				break			
	#print(apendice)
	#print(matrizMov)


def functionCuadroJugador(coorMov,coorCuadrosReales):
  #formando la subcadena
  subcoorMovJ = []
  print("longitud ", len(coorMov))
  x = 0 
  while(x < len(coorMov) ):
    subcoorMovJ.append( [coorMov[x], coorMov[x+1]] )
    x = x+2
  print("en dos coorMov: ", subcoorMovJ)
    
  auxCoorCr = np.array([])
    
  cadenaLast = subcoorMovJ[len(subcoorMovJ)-1]
  print(cadenaLast)
  arraySupervision = []
  
  for j1 in range(0,len(coorCuadrosReales)):
    auxCoorCr = coorCuadrosReales[j1]
    for j2 in range(0,4):
      if cadenaLast[0] == auxCoorCr[j2][0]  and cadenaLast[1] == auxCoorCr[j2][1]:
        arraySupervision.append(auxCoorCr)
        break
  
  print("posibles cuadros: ", arraySupervision)
  
  # buscando si en coorMovJ  esta en algun cuadro de arraySupervision
  auxSup = []
  contadorCJ = 0
  for j3 in range(0,len(arraySupervision)):
    auxSup = arraySupervision[j3]
    contadorCJ = 0
    for j4 in range(0,4): # nivel: se mueve en las cordenadas del cuadro 0
      for j5 in range(0,len(subcoorMovJ)): # nivel: lo busca en las coordenadas de movimiento coorMov
        if auxSup[j4][0] == subcoorMovJ[j5][0] and auxSup[j4][1] == subcoorMovJ[j5][1]:
          contadorCJ = contadorCJ + 1
          break
    if contadorCJ == 4:
      #puntosJugador = puntosJugador + 1
      break
  
  if contadorCJ != 4: # ningun cuadro formado por el jugador
    auxSup = []
  
  return auxSup

#################################################
#### VAMOS A CREAR UNA MATRIZ DE LAS COORDENADAS DE LOS CUADROS 
coorCuadros = []
#n = 6
salto = 0
xn = 0
for x in range(1,numCuadros+1):
  xn = xn + 1
  if xn%n == 0 :
    xn = xn+1
  coorCuadros.append([xn, xn+1, n+xn, (n+xn)+1])

print("coordenada de cuadros ", coorCuadros)
	
coorCuadrosReales = []
ayudaCR = []
	
for ic in range(0,len(coorCuadros)):
  ayudaCR.append([coorCuadros[ic][0], coorCuadros[ic][1]])
  ayudaCR.append([coorCuadros[ic][2], coorCuadros[ic][3]])
  ayudaCR.append([coorCuadros[ic][0], coorCuadros[ic][2]])
  ayudaCR.append([coorCuadros[ic][1], coorCuadros[ic][3]])
  
  coorCuadrosReales.append(ayudaCR)
  ayudaCR = [] 

print("coordenada de cuadros Real", coorCuadrosReales)
#################################################

## inicio del juego
coorMov = []
puntosComputadora = 0
puntosJugador = 0
pasos = 0
OPERADORES = np.array(OPERADORES1)
pasosi = 0
ENDGAME = 0
contadorCUADRO = 0
GANADOR = ''
cuadrosJugador = []
cuadrosComputadora = []

print("")
print(" ************   INICIO DEL JUEGO     ************ ")
print (" INGRESE LAS COORDENADASDE MOVIMIENTOS  ")
print("")

auxSup = []

while ENDGAME == 0:
	if contadorCUADRO != 3:   #funcion de retorno
		xMovs = input(" introduce inicio de linea: ")    
		yMovs = input(" introduce final de linea: ")
		
		xMov = int(xMovs)
		yMov = int(yMovs)
		
		aux123 = 0
		
		if xMov > yMov:
		  aux123 = xMov
		  xMov = yMov
		  yMov = aux123 

		coorMov.append(xMov)
		coorMov.append(yMov)
		
		# checando si acabas de formar un cuadro para así dar otro turno de tiro
		# la referencia es el ultimo tiro ;)
		
		auxSup = functionCuadroJugador(coorMov,coorCuadrosReales)#,puntosJugador)
		
		while auxSup != []: # ha formado un cuadro nuevo
		  if len(coorMov) == constante:
		    ENDGAME = 1
		    if puntosComputadora > puntosJugador :
		      GANADOR = 'COMPUTADORA'
		    if puntosComputadora < puntosJugador :
		      GANADOR = 'GANASTE! :)'
		    auxSup = []
		    print("FIN DEL JUEGO")
		  
		  puntosJugador = puntosJugador + 1
		  print("Hizo un punto * ")
		  print("Puntos sumados: ", puntosJugador )
		  print("Vuelva a tirar")
		  
		  xMovs = input(" introduce inicio de linea ")    
		  yMovs = input(" introduce final de linea ")
		  
		  xMov = int(xMovs)
		  yMov = int(yMovs)
		  aux123 = 0
		  if xMov > yMov:
		    aux123 = xMov
		    xMov = yMov
		    yMov = aux123
		  
		  coorMov.append(xMov)
		  coorMov.append(yMov)
		  
		  
		  auxSup = functionCuadroJugador(coorMov,coorCuadrosReales)#,puntosJugador)
		
		print("cuadro formado es: ", auxSup)
		  

	print("sin eliminar: ", OPERADORES1)

  
	print("movidas", coorMov)
	for coor in range(pasosi,len(coorMov)-1):
		for x in range(0,len(OPERADORES)):
			for y in range(0,len(OPERADORES[x])):
				if (x+1 == coorMov[coor]) and (OPERADORES[x][y] == coorMov[coor+1]):
					OPERADORES[x] = np.delete(OPERADORES[x],y)
					break
				if (x+1 == coorMov[coor+1]) and (OPERADORES[x][y] == coorMov[coor]):
					OPERADORES[x] = np.delete(OPERADORES[x],y)
					break
					

	print("matriz de CONOCIMIENTO: ", OPERADORES)   #### MATRIZ DE CONOCIMIENTO ####

	#HEURISTICA 3 eleccion de movimientos de la computadora xMovComp yMovComp

	#1era HEURISTICA no entrar a formar parte de las lineas para no formar un cuadro

	print("coorMov: ", coorMov)
	print("coorMov: ", len(coorMov))


	OPheuristica = np.array(OPERADORES)
	numEliminados = 0

	for x in range(0,len(coorMov)):
		#OPheuristica = np.delete(OPheuristica,(coorMov[x] - (x+1)))
		for j in range(0,len(OPheuristica)):
			if j+1 == coorMov[x]:
				OPheuristica[j] = [] 

	print("OPERADORES ELIM: ", OPheuristica)
	check = 0
	for x in range(0,len(OPheuristica)):
		if OPheuristica[x] != []:
			check = 1   ## VEMOS SI AÚN ES VALIDA ESTA HEURISTICA 
		
	if check == 0:
		OPheuristica = np.array(OPERADORES)

	print("OPERADORES ELIM con posible correccion: ", OPheuristica)

	#2da HEURISTICA los que tengan mayor longitud 
	maximo = []
	for x in range(0,len(OPheuristica)):
		maximo.append(len(OPheuristica[x]))

	maxi = max(maximo) #encontramos el maximo
	cadenaMaxi = np.array([])
	print("cadena de longitud ", maxi)

	for xMaxima in range(0,len(maximo)): #buscamos al maximo e indirectamente el indice para asi encontrar al maz en OPERADOR
		if maxi == maximo[xMaxima]:
			cadenaMaxi = np.array(OPheuristica[xMaxima])
			pivote = xMaxima + 1 
			break
	print("cadena a revisar", cadenaMaxi)
	#3er HEURISTICA se elije la linea más alejada a los puntos ya escritos 

	#3.1 que no sea adyacente a ninguno de ellos

	a = 0
	b = 0
	i = 0
	resultado = []
	for i in range(0,len(coorMov)):
		for j in range(0,len(cadenaMaxi)):
			if cadenaMaxi[j] == coorMov[i] :
				cadenaMaxi[j] = 0

	print("cadena a revisar", cadenaMaxi)
	check = 0
	for x in range(0,len(cadenaMaxi)): #checamos si la cadena ha quedado borrada y ya no hay más opciones 
		if cadenaMaxi[x] != 0:
			check = 1

	if check == 0:  #si la cadena resulto ser vacia usamos la cadena normal  
		cadenaMaxi = OPheuristica[xMaxima]

	print("cadena a revisar desicion ", cadenaMaxi)

	#3.2 que no comience a formar un cuadro
		#### VAMOS A CREAR UNA MATRIZ DE LAS COORDENADAS DE LOS CUADROS 
	coorCuadros = []
	#n = 6
	salto = 0
	xn = 0
	for x in range(1,numCuadros+1):
		xn = xn + 1
		if xn%n == 0 :
			xn = xn+1
		coorCuadros.append([xn, xn+1, n+xn, (n+xn)+1])
	
	print("coordenada de cuadros ", coorCuadros)

	# buscando que no se forme un cuadro
	for jj in range(0,len(coorCuadros)):
		if (coorMov[0] in coorCuadros[jj]) and (coorMov[1] in coorCuadros[jj]):
			break
	print("coorCuadros",coorCuadros[jj])

	cuadroElim = np.array(coorCuadros[jj])
	cuadroElim = np.delete(cuadroElim, coorMov[0])
	cuadroElim = np.delete(cuadroElim, coorMov[1])
	print("cuadroElim ", cuadroElim)

	for x in range(0,len(cadenaMaxi)):
		if cadenaMaxi[x] in cuadroElim or cadenaMaxi[x] == 0:
			pass
		else:
			break
			
	if pivote < cadenaMaxi[x]:
	  xMovComp = pivote
	  yMovComp = cadenaMaxi[x]
	else:
	  yMovComp = pivote
	  xMovComp = cadenaMaxi[x]
		
	#3.3 si se está a punto de formar un cuadro nos ponemos ahí 
	# buscando si se esta formando un cuadro"!
	# formando coordenadas reales de cada cuadro ;)
	
	coorCuadrosReales = []
	ayudaCR = []
	
	for ic in range(0,len(coorCuadros)):
	  ayudaCR.append([coorCuadros[ic][0], coorCuadros[ic][1]])
	  ayudaCR.append([coorCuadros[ic][2], coorCuadros[ic][3]])
	  ayudaCR.append([coorCuadros[ic][0], coorCuadros[ic][2]])
	  ayudaCR.append([coorCuadros[ic][1], coorCuadros[ic][3]])
	  
	  coorCuadrosReales.append(ayudaCR)
	  ayudaCR = [] 
	  
	print("coordenada de cuadros Real", coorCuadrosReales)
	
	#formando la subcadena
	subcoorMov = []
	print("longitud ", len(coorMov))
	x = 0 
	while(x < len(coorMov) ):
	  subcoorMov.append( [coorMov[x], coorMov[x+1]] )
	  x = x+2
	
	print("subcadena de movimientos", subcoorMov)	
	
	#buscando si algun pre cuadro = cuadro - un lado existe en subcoorMov

	contadorCUADRO = 0
	ayudaPreCuadro = []
	
	for x in range(0,len(coorCuadrosReales)):
	  contadorCUADRO = 0
	  ayudaPreCuadro = []
	  for y in range(0,len(subcoorMov)):
	    if subcoorMov[y] in coorCuadrosReales[x]:
	      contadorCUADRO = contadorCUADRO + 1
	      ayudaPreCuadro.append(subcoorMov[y])
	    
	  if contadorCUADRO == 3:
	    break
	  
	print("cuadro posible ", coorCuadrosReales[x])
	print("pre cuadro exist ", ayudaPreCuadro)
	  
	borr = np.array(coorCuadrosReales[x])
	borr1 = np.array([])
	bandera = 0
	
	#tomando la coordenada de jugada para cerrar el cuadro
  
	mi = 0
	auxBorr = np.array([])
	auxPreCuadro = np.array([])
  
	if contadorCUADRO == 3:
	  cuadrosComputadora.append(borr)
	  for mi in range(0,len(borr)):
	    bandera = 0
	    auxBorr = np.array(borr[mi])
	    for nj in range(0,len(ayudaPreCuadro)):
	      auxPreCuadro = np.array(ayudaPreCuadro[nj])
	      if (auxBorr[0] == auxPreCuadro[0]) and (auxBorr[1] == auxPreCuadro[1]) :
	        bandera = 1 # ya lo encontro	
	      if bandera == 1:
	        break
	    if bandera == 0:
	      break
    
   
	  borr1 = np.array(borr[mi])
	  xMovComp = borr1[0]
	  yMovComp = borr1[1]
	  puntosComputadora = puntosComputadora + 1
	  
	 
	print("precuadro ", borr[mi])
	print("coordenadas cuadro reales limpio ", coorCuadrosReales)
  
	coorMov.append(xMovComp)
	coorMov.append(yMovComp)
	

	print("maximo ", maximo)
	print("maxi ", maxi)
	print("pivote: ", pivote)
	print("maxima cadena ", cadenaMaxi)
	print(coorCuadros)
	print("")
	print("**********")
	print("MOVIMIENTOS: ", coorMov)
	print("puntos de la computadora: ", 	puntosComputadora)
	print("puntos deL JUGADOR: ", 	puntosJugador)
	
	#fin del juego
	#checando la matriz de conocimiento SI ESTÁ VACÍA TERMINO EL JUEGO
	FINAL = 0
	for x in range(0,len(OPERADORES)):
	  if OPERADORES[x] != []:
	    FINAL = 1
	    
	if len(coorMov) == constante:
	  ENDGAME = 1
	  if puntosComputadora > puntosJugador :
	    GANADOR = 'COMPUTADORA'
	  if puntosComputadora < puntosJugador :
	    GANADOR = 'GANASTE! :)'
	  print("FIN DEL JUEGO")

	pasos = pasos + 1
	pasosi = pasosi +2
	
	
print("MOVIMIENTOS:  ", coorMov )

movClaros = []
xf = 0
while(xf < len(coorMov)):
  movClaros.append([coorMov[xf], coorMov[xf+1]])
  xf = xf + 2

print("")
print("   ********   FIN DEL JUEGO   *********  ")
print("Historial de movimientos", movClaros)
print("")
print("   ********   RESUMEN DEL JUEGO:   *********  ")
print("")
print("Puntos del jugador: ", 	puntosJugador )
print("Puntos de la computadora: ", 	puntosComputadora )
print("GANADOR: ", GANADOR )

print("Cuadros de la computadora: ", cuadrosComputadora)





