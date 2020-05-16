import numpy
import matplotlib.pyplot as plt
import random
from scipy import stats
import math

varianza=0
desvio=0
frecrelativa=0
media=0
contador2=0

for i in range(5):
	NumeroElegido=random.randint(0,36)  #El numero se elige al azar
	lista=[]
	listaMedia=[]
	mediaGrafico=[]
	listaVarianza=[]
	varianzaGrafico=[]
	listaDesvio=[]
	desvioGrafico=[]
	listaFR=[]
	frGrafico=[]
	contador=0
	varianzaTemp=0
	desvioTemp=0
	for j in range(10000):
		aleatorio=random.randint(0,36)
		lista.append(aleatorio)
		listaMedia.append(numpy.mean(lista))
		if aleatorio!=NumeroElegido:
			listaVarianza.append(varianzaTemp)
			listaDesvio.append(desvioTemp)
			listaFR.append(frecrelativa)
		else:
			varianzaTemp=numpy.var(lista)
			desvioTemp=numpy.std(lista)
			contador=contador+1
			frecrelativa=contador/j
			listaVarianza.append(varianzaTemp)
			listaDesvio.append(desvioTemp)
			listaFR.append(frecrelativa)

	media=numpy.mean(lista)+media
	varianza=numpy.var(lista) +varianza
	desvio=numpy.std(lista)	+desvio

	plt.figure("media")
	plt.plot(listaMedia,label="valor promedio de las tiradas respecto a n")
	plt.legend()
	plt.title("Grafico de valor promedio de las tiradas respecto al numero de tiradas")   #  título del gráfico
	plt.xlabel("n: Numero de tiradas")   #  título del eje x
	plt.ylabel("vp: Valor promedio de las tiradas")   # título del eje y


	plt.figure("desvio")
	plt.plot(listaDesvio,label="valor del desvio del numero "+str(NumeroElegido)+" con respecto a n")
	plt.legend()
	plt.title("Grafico del desvio respecto al numero de tiradas")   
	plt.xlabel("n: Numero de tiradas")   
	plt.ylabel("vd: Valor del desvio")   

	plt.figure("varianza")
	plt.plot(listaVarianza,label="valor de la varianza del numero "+str(NumeroElegido)+" con respecto a n")
	plt.legend()
	plt.title("Grafico de la varianza respecto al numero  de tiradas")   
	plt.xlabel("n: Numero de tiradas")   
	plt.ylabel("vv: Valor de la varianza")  

	plt.figure("frecrelativa")
	plt.plot(listaFR,label="frecuencia relativa del numero "+str(NumeroElegido)+" respecto a n")
	plt.legend()
	plt.title("Grafico de la frecuencia relativa  respecto al numero de tiradas")   
	plt.xlabel("n: Numero de tiradas")   
	plt.ylabel("fr: Frecuencia relativa  " )   

	contador2=contador2+1
for i in range (10000):
	mediaGrafico.append(media/contador2)
	varianzaGrafico.append(varianza/contador2)
	desvioGrafico.append(desvio/contador2)
	frGrafico.append(1/37)

plt.figure("media")
plt.plot(mediaGrafico,label="valor promedio esperado de las medias")
plt.legend()
plt.savefig("Media.png")
plt.figure("desvio")
plt.plot(desvioGrafico,label="valor promedio esperado de los desvios")
plt.legend()
plt.savefig("Desvio.png")
plt.figure("varianza")
plt.plot(varianzaGrafico,label="valor promedio  esperado de las varianzas")
plt.legend()
plt.savefig("Varianza.png")
plt.figure("frecrelativa")
plt.plot(frGrafico,label="frecuencia relativa promedio esperada de las frecuencias relativas ")
plt.legend()
plt.savefig("FrecRelat.png")


lista=[]
listaMedia=[]
mediaGrafico=[]
listaVarianza=[]
varianzaGrafico=[]
listaDesvio=[]
desvioGrafico=[]
listaFR=[]
frGrafico=[]
varianza=0
desvio=0
frecrelativa=0
contador=0
NumeroElegido=random.randint(0,36)  #El numero se elige al azar


for i in range(10000):
	aleatorio=random.randint(0,36)
	lista.append(aleatorio)
	listaMedia.append(numpy.mean(lista))
	if aleatorio!=NumeroElegido:
		listaVarianza.append(varianza)
		listaDesvio.append(desvio)
		listaFR.append(frecrelativa)
	else:
		varianza=numpy.var(lista)
		desvio=numpy.std(lista)
		contador=contador+1
		frecrelativa=contador/i
		listaVarianza.append(varianza)
		listaDesvio.append(desvio)
		listaFR.append(frecrelativa)

media=numpy.mean(lista)
mediana=numpy.median(lista) #no se grafica
varianza=numpy.var(lista)
desvio=numpy.std(lista)
moda=stats.mode(lista)	#no se grafica pero igual lo colocamos , como la mediana
print("Numeros de la ruleta  : ")
print (lista) #todos los numeros aleatorios
print("Media esperada: "+str(media))	#Media
print("Mediana: "+str(mediana)) #Mediana
print("Varianza esperada: "+str(varianza))	  #Varianza
print("Desvio esperado: "+str(desvio))	#desvio estandar
print("Moda: ")
print(moda) #Moda 

for i in range (10000):
	mediaGrafico.append(media)
	varianzaGrafico.append(varianza)
	desvioGrafico.append(desvio)
	frGrafico.append(1/37)

plt.figure("media2")
plt.plot(listaMedia,label="valor promedio de las tiradas respecto a n")
plt.legend()
plt.title("Grafico de valor promedio de las tiradas respecto al numero de tiradas")   #  título del gráfico
plt.xlabel("n: Numero de tiradas")   #  título del eje x
plt.ylabel("vp: Valor promedio de las tiradas")   # título del eje y
plt.plot(mediaGrafico,label="valor promedio esperado")
plt.legend()

plt.savefig("Media2.png")

plt.figure("desvio2")
plt.plot(listaDesvio,label="valor del desvio del numero "+str(NumeroElegido)+" con respecto a n")
plt.legend()
plt.title("Grafico del desvio respecto al numero de tiradas")   
plt.xlabel("n: Numero de tiradas")   
plt.ylabel("vd: Valor del desvio")   
plt.plot(desvioGrafico,label="valor del desvio esperado")
plt.legend()

plt.savefig("Desvio2.png")

plt.figure("varianza2")
plt.plot(listaVarianza,label="valor de la varianza del numero "+str(NumeroElegido)+" con respecto a n")
plt.legend()
plt.title("Grafico de la varianza respecto al numero  de tiradas")   
plt.xlabel("n: Numero de tiradas")   
plt.ylabel("vv: Valor de la varianza")  
plt.plot(varianzaGrafico,label="valor de la varianza esperada")
plt.legend()

plt.savefig("Varianza2.png")

plt.figure("frecrelativa2")
plt.plot(listaFR,label="frecuena relativa del numero "+str(NumeroElegido)+" respecto a n")
plt.legend()
plt.title("Grafico de la frecuencia relativa  respecto al numero de tiradas")   
plt.xlabel("n: Numero de tiradas")   
plt.ylabel("fr: Frecuencia relativa  " )   
plt.plot(frGrafico,label="frecuencia relativa esperada de "+str(NumeroElegido))
plt.legend()

plt.savefig("FrecRelat2.png")

plt.show()


