import math
import random
import matplotlib.pyplot as plt
import numpy 

# En nuestro trabajo seleccionamos que el jugador ganaria si la ruleta cae en un numero impar.
# En el caso de que la ruleta caiga en un numero par o  0 , el casino ganara.
#Esto indica que el casino tendra una ventaja clara, ya que tendra una probabilidad de ganar de 19/37 
# Mientras que el jugador tendra una probabilidad de 18/37
#Los resultados que ocurren cuando existe una apuesta maxima y cuando no  , son mas que notables.



def MartinGala(apuestaBase,dineroInicial,infinito):
	listaFr=[]
	rachaPerdidas=0 			  # Racha de perdidas
	contador=0
	resultados=[]	#Arreglo con todos los resultados de las jugadas[dinero total acumulado]
	frcrelativa=0
	rachaPerdidas=0
	dineroTotal=dineroInicial
	for i in range(10000):
		NumeroElegido=random.randint(0,36)
		apuesta=apuestaBase* 2**(rachaPerdidas) #Apuesta en base la racha de perdidas
		if (apuesta>dineroTotal and infinito==False):
			apuesta=dineroTotal

		if ((NumeroElegido % 2 )!=0):
			rachaPerdidas=0
			dineroTotal+=apuesta
			contador+=1
			frcrelativa=contador/(i+1)
		else:
			rachaPerdidas=rachaPerdidas+1
			dineroTotal-=apuesta

		listaFr.append(frcrelativa)
		resultados.append(dineroTotal)
		if(dineroTotal==0 and infinito==False):
			break

	return resultados,listaFr,dineroInicial


resultados, listaFr, dineroInicial = MartinGala(1, 0, True)
listaDineroInicial=[]
for i in range(len(resultados)):
	listaDineroInicial.append(dineroInicial)
plt.figure("LineaInfinita")
plt.plot(resultados,label="Flujo de caja")
plt.legend()
plt.title("Martin Gala sin limite de presupuesto")   
plt.xlabel("n (Numero de tiradas)")   
plt.ylabel("Beneficio acumulado")
plt.savefig("LineaInfinitaMG.png")

plt.figure("Frecuencia Relativa infinita")
plt.plot(listaFr, label="frsa (Frecuencia relativa de obtener la apuesta favorable segun n)")
plt.legend()
plt.title("Martin Gala sin limite de presupuesto")
plt.xlabel("n (Numero de tiradas)")
plt.ylabel("fr (Frecuencia relativa)")

plt.savefig("FRINFINITA_MG.png")

plt.figure("LineasInfinitasMG")
for j in range (5):
	resultados, listaFr, dineroInicial = MartinGala(1, 0, True)
	plt.plot(resultados,label="Flujo de caja de la curva "+ str(j+1))
	plt.legend()
	plt.title("Martin Gala sin limite de presupuesto")   
	plt.xlabel("n (Numero de tiradas)")   
	plt.ylabel("Beneficio acumulado")
plt.savefig("LineasInfinitasMG.png")

resultados, listaFr, dineroInicial = MartinGala(1, 1000, False)
listaDineroInicial=[]
for i in range(len(resultados)):
	listaDineroInicial.append(dineroInicial)
plt.figure("LineaFinita")
plt.plot(resultados,label="Flujo de caja")
plt.legend()
plt.title("Martin Gala con limite de presupuesto")   
plt.xlabel("n (Numero de tiradas)")   
plt.ylabel("Cantidad de capital")
plt.plot(listaDineroInicial,label="Flujo de caja inicial")
plt.legend()
plt.savefig("LineafinitaMG.png")

plt.figure("Frecuencia Relativa Finita")
plt.plot(listaFr, label="frsa (Frecuencia relativa de obtener la apuesta favorable segun n)")
plt.legend()
plt.title("Martin Gala con limite de presupuesto")
plt.xlabel("n (Numero de tiradas)")
plt.ylabel("fr (Frecuencia relativa)")

plt.savefig("FRFINITA_MG.png")

plt.figure("LineasfinitasMG")
listaDineroInicial=[]
for j in range (5):
	resultados, listaFr, dineroInicial = MartinGala(1, 1000, False)
	plt.plot(resultados,label="Flujo de caja de la curva "+ str(j+1))
	plt.legend()
	plt.title("Martin Gala con limite de presupuesto")   
	plt.xlabel("n (Numero de tiradas)")   
	plt.ylabel("Cantidad de capital")
for i in range(10000):
		listaDineroInicial.append(dineroInicial)
plt.plot(listaDineroInicial,label="Flujo de caja inicial")
plt.legend()
plt.savefig("LineasfinitasDL.png")
plt.savefig("LineasfinitasMG.png")



def DAlembert(apuestaBase,dineroInicial,infinito):
	listaFr=[]
	rachaPerdidas=0 			  # Racha de perdidas
	contador=0
	resultados=[]	#Arreglo con todos los resultados de las jugadas
	frcrelativa=0
	rachaPerdidas=0
	dineroTotal=dineroInicial
	apuesta=apuestaBase
	for i in range(5000):
		NumeroElegido=random.randint(0,36)
		if (apuesta>dineroTotal and infinito==False):
			apuesta=dineroTotal

		if ((NumeroElegido % 2 )!=0):
			rachaPerdidas=0
			dineroTotal+=apuesta
			apuesta-=1
			contador+=1
			frcrelativa=contador/(i+1)
		else:
			rachaPerdidas=rachaPerdidas+1
			dineroTotal-=apuesta
			apuesta+=1

		listaFr.append(frcrelativa)
		resultados.append(dineroTotal)
		if(dineroTotal==0 and infinito==False):
			break

	return resultados,listaFr,dineroInicial


resultados, listaFr, dineroInicial = DAlembert(5, 0, True)
listaDineroInicial=[]
for i in range(len(resultados)):
	listaDineroInicial.append(dineroInicial)
plt.figure("LineaInfinita2")
plt.plot(resultados,label="Flujo de caja")
plt.legend()
plt.title("d'ALembert sin limite de presupuesto")   
plt.xlabel("n (Numero de tiradas)")   
plt.ylabel("Beneficio acumulado")
plt.savefig("LineaInfinitaDL.png")

plt.figure("Frecuencia Relativa infinita2")
plt.plot(listaFr, label="frsa (Frecuencia relativa de obtener la apuesta favorable segun n)")
plt.legend()
plt.title("d'ALembert sin limite de presupuesto")
plt.xlabel("n (Numero de tiradas)")
plt.ylabel("fr (Frecuencia relativa)")
plt.savefig("FRINFINITA_DL.png")

plt.figure("LineasInfinitasDL")
for j in range (5):
	resultados, listaFr, dineroInicial = DAlembert(5, 0, True)
	listaDineroInicial=[]
	plt.plot(resultados,label="Flujo de caja de la curva "+ str(j+1))
	plt.legend()
	plt.title("d'ALembert sin limite de presupuesto")   
	plt.xlabel("n (Numero de tiradas)")   
	plt.ylabel("Beneficio acumulado")
plt.savefig("LineasInfinitasDL.png")

resultados, listaFr, dineroInicial = DAlembert(5, 1000, False)
listaDineroInicial=[]
for i in range(len(resultados)):
	listaDineroInicial.append(dineroInicial)
plt.figure("LineaFinita2")
plt.plot(resultados,label="Flujo de caja")
plt.legend()
plt.title("d'ALembert con limite de presupuesto")   
plt.xlabel("n (Numero de tiradas)")   
plt.ylabel("Cantidad de capital")
plt.plot(listaDineroInicial,label="Flujo de caja inicial")
plt.legend()
plt.savefig("LineafinitaDL.png")

plt.figure("Frecuencia Relativa Finita2")
plt.plot(listaFr, label="frsa (Frecuencia relativa de obtener la apuesta favorable segun n)")
plt.legend()
plt.title("d'ALembert con limite de presupuesto")
plt.xlabel("n (Numero de tiradas)")
plt.ylabel("fr (Frecuencia relativa)")
plt.savefig("FRFINITA_DL.png")

plt.figure("LineasfinitasDL")
listaDineroInicial=[]
for j in range (5):
	resultados, listaFr, dineroInicial = DAlembert(5, 1000, False)
	plt.plot(resultados,label="Flujo de caja de la curva "+ str(j+1))
	plt.legend()
	plt.title("d'ALembert con limite de presupuesto")   
	plt.xlabel("n (Numero de tiradas)")   
	plt.ylabel("Cantidad de capital")
for i in range(5000):
		listaDineroInicial.append(dineroInicial)
plt.plot(listaDineroInicial,label="Flujo de caja inicial")
plt.legend()
plt.savefig("LineasfinitasDL.png")




plt.show()
