import random
import numpy
from scipy.stats.distributions import chi2
import os
import math
import matplotlib.pyplot as plt
#Generacion Cuadrado Medio

def CuadradoMedio():
	x=[]
	u=[]
	x.append(random.randint(1000,9999))
	u.append("{0:.5f}".format(x[0]/10000))
	for i in range(1,15000):
		x.append(cortarCentro(x[i-1]*x[i-1]))
		u.append("{0:.5f}".format(x[i]/10000))
	return u


def cortarCentro(numero):
    centro = numero//100
    centro = centro-((centro)//10000)*10000
    return centro

# x=CuadradoMedio()
# for i in range(len(x)):
# 	print(x[i])

#Generacion de numeros aleatorios RAND

def sucesionRand():
	x=[]
	u=[]
	x.append(random.randint(0,2**31-1))
	u.append(x[0]/(2**31-1))
	for i in range(1,15000):
		x.append((7**5 *x[i-1])%(2**31-1))
		u.append(x[i]/(2**31-1))
	return u
# for i in range(len(u)):
# 	print(u[i])


#Generacion de numeros aleatorios RANDU
def sucesionRandu():
	x=[]
	u=[]
	x.append(random.randint(0,2**31-1))
	u.append(x[0]/(2**31-1))
	for i in range(1,15000):
		x.append(((2**16+3)*x[i-1])%(2**31))
		u.append(x[i]/(2**31))
	return u
# u=sucesionRandu()

# for i in range(len(u)):
# 	print(u[i])

# Generador GCL
def gcl():
	m = (2**31-1)
	a = 7**5
	c = 11
	y=[]
	x=[]
	u=[]
	x.append(random.randint(0, 2**31-1))
	u.append(x[0]/((2**31)-1))
	for i in range(1,15000):
		x.append((a * x[i-1] + c) % m)
		u.append(x[i]/((2**31)-1))
	return u


# u = gcl()
# for i in range(len(u)):
# 	print(u[i])
#TEST CHI CUADRADO
def TestChiCuad(u):
	print("Test de bondad Chi Cuadrado")
	observado=[]
	esperado=1500
	c=0.1
	for i in range (10):
		x =0
		for j in range (len(u)):
			if  (c-0.1)<=float(u[j])<=c:
				x+=1
		observado.append(x)
		c+=0.1
	x2=0
	for i in range(len(observado)):
		x2+=(((observado[i]-esperado)**2)/esperado)
	print("X2 = "+ str(x2))
	#print(1-chi2.sf(x2, 8))



def testPoker(u,sucesion):
	print("Test de Poker")
	x=[]
	y=[]
	z=[]
	for i in range(100):
		s = verificarSucesion(sucesion)
		distintos,dosIguales,tresIguales=pokerCaracteres(s)
		x.append(distintos)
		y.append(dosIguales)
		z.append(tresIguales)
	
	distintos, dosIguales, tresIguales = pokerCaracteres(u)
	totalDistintos=pokerSuma(distintos,numpy.mean(x))
	totalDosIguales = pokerSuma(dosIguales, numpy.mean(y))
	totalTresIguales= pokerSuma(tresIguales, numpy.mean(z))
	x2=totalDistintos+totalDosIguales+totalTresIguales
	print("X2 = "+ str(x2))
#	print(1-chi2.sf(x2, 2))



def pokerCaracteres(u):
	distintos = 0
	dosIguales = 0
	tresIguales = 0
	for i in range(len(u)):
		c = str(u[i])
		if(c[2] != c[3] and c[2] != c[4] and c[3] != c[4]):
			distintos += 1
		elif(c[2] == c[3] and c[2] == c[4] and c[3] == c[4]):
			tresIguales += 1
		else:
			dosIguales += 1
	return distintos,dosIguales,tresIguales

def pokerSuma(observado,esperado):
	return(((observado-esperado)**2)/esperado)

def verificarSucesion(sucesion):
	if sucesion=="rand":
		u=sucesionRand()
	elif sucesion=="randu":
		u=sucesionRandu()
	elif sucesion=="cuadrado":
		u=CuadradoMedio()
	elif sucesion =="gcl":
		u=gcl()
	elif sucesion == "random":
		u = ArregloRandom()
	return u


def testCorridas(u):
	print("Test de Corridas: ")
	x = []
	a = 1
	for i in range(len(u)-1):
		if u[i+1] >= u[i]:
			x.append("+")
		elif(u[i+1] < u[i]):
			x.append("-")

	for i in range(1, len(x)):
		if (x[i] != x[i-1]):
			a += 1
	n = len(x)
	media = (2*n-1)/3
	desviacion = math.sqrt((16*n-29)/90)
	z = (a-media)/desviacion
	print("Z <= "+ str(z))


def testArribaAbajo(p):
	print("Test arriba y abajo : ")
	x = []
	corridas = 1
	contmas = 0
	contmenos = 0
	u=[]
	
	for i in range(len(p)-1):
		u.append(float(p[i]))
	med=numpy.mean(u)

	for i in range(len(u)):
		if u[i] >= med:
			x.append("+")
		elif(u[i] < med):
			x.append("-")

	for i in range(1, len(x)):
		if (x[i] != x[i-1]):
			corridas += 1

	if  (x[0]=="+"):
		contmas+=1
	else:
		contmenos+=1
	for i in range(1,len(x)):
		if(x[i] == "+"):
			contmas += 1
		else:
			contmenos += 1

	n = contmas+contmenos
	media = ((2*contmenos*contmas)/(contmas+contmenos))+1
	desviacion = math.sqrt(((2*contmenos*contmas*(2*contmas*contmenos-n))/((n**2)*(n-1))))
	z = (corridas-media)/desviacion
	print("Z <=" + str(z) )

def ArregloRandom():
	u=[]
	for i in range(15000):
		u.append(random.random())
	return u

# Para las pruebas: 
# -En el test de bondad de Chi cuadrado con un 95 % de certeza , para que que el test sea correcto el X2 calculado
# debe ser menor a 16.92
# -En el test de Poker con un 95% de certeza , para que el test sea correcto el x2 calculado debe ser menor a 5.99
# -En el test de Corridas y el de arriba y abajo Z<1.96 para que tire una hipotesis correcta.



def graficarDispersion(u,titulo):
	x = []
	for i in range(15000):
		x.append(i)
	plt.scatter(x,u ,color='y',marker='*',s=2)
	if (titulo=="rand"):
		plt.scatter(x, u, color='y', marker='*', s=2)
		plt.title("Muestra Rand")
	elif (titulo=="randu"):
		plt.scatter(x, u, color='b', marker='*', s=2)
		plt.title("Muestra Randu")
	elif (titulo=="gcl"):
		plt.scatter(x, u, color='purple', marker='*', s=2)
		plt.title("Muestra GCL generico")
	elif (titulo=="cuadrado"):
		plt.scatter(x, u, color='g', marker='*', s=2)
		plt.title("Muestra cuadrado medio")
	elif (titulo =="python"):
		plt.scatter(x, u, color='r', marker='*', s=2)
		plt.title("Muestra de generador propio de python")
	plt.xlabel("Numero de repetición")
	plt.ylabel("valor")
	plt.show()

	

def menu():
    print(" ")
    print("MENÚ PRINCIPAL - Seleccione una opción")
    print("1 - Rand")
    print("2 - RandU")
    print("3 - GCL")
    print("4 - Cuadrado Medio")
    print("5 - Generador Random() de Python")
    print("0 - Salir")

while True:
	os.system('cls')

	menu()

	opcionMenu = input("Ingrese su opcion:  ")
	print(" ")

	if opcionMenu == "1" : 
		u = sucesionRand()
		graficarDispersion(u,"rand")
		for i in range(len(u)):
			print(u[i])
		TestChiCuad(u)
		testPoker(u,"rand")
		testCorridas(u)
		testArribaAbajo(u)
		input("Pulsa una tecla para continuar")

	elif opcionMenu == "2":
		u = sucesionRandu()
		graficarDispersion(u,"randu")
		for i in range(len(u)):
			print(u[i])
		TestChiCuad(u)
		testPoker(u, "randu")
		testCorridas(u)
		testArribaAbajo(u)
		input("Pulsa una tecla para continuar")

	elif opcionMenu == "3":
		u = gcl()
		graficarDispersion(u,"gcl")
		for i in range(len(u)):
			print(u[i])
		TestChiCuad(u)
		testPoker(u, "gcl")
		testCorridas(u)
		testArribaAbajo(u)
		input("Pulsa una tecla para continuar")

	elif opcionMenu == "4":
		u = CuadradoMedio()
		graficarDispersion(u,"cuadrado")
		for i in range(len(u)):
			print(u[i])
		TestChiCuad(u)
		testPoker(u, "cuadrado")
		testCorridas(u)
		testArribaAbajo(u)
		input("Pulsa una tecla para continuar")
	elif opcionMenu == "5":
		u = ArregloRandom()
		graficarDispersion(u,"python")
		for i in range(len(u)):
			print(u[i])
		TestChiCuad(u)
		testPoker(u, "random")
		testCorridas(u)
		testArribaAbajo(u)
		input("Pulsa una tecla para continuar")
	elif opcionMenu == "0":
		break

	else:
		print(" ")
		input("No has pulsado ninguna opción correcta... \n Pulsa una tecla para continuar")

		
	


