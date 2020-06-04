import random
import matplotlib.pyplot as plt
import  math
import numpy as np
from scipy.stats import norm
import scipy.stats


def generadorRandu():
    x = []
    u = []
    x.append(random.randint(0, 2**31-1))
    u.append(x[0]/(2**31-1))
    for i in range(1, 1000):
        x.append(((2**16+3)*x[i-1]) % (2**31))
        u.append(x[i]/(2**31))
    return u

def uniforme (a,b):
    x=[]
    for i in range(1000):
        r = round(random.random(), 4)
        x.append(a+(b-a)*r)
    return x

uni=(uniforme(1,3))

# X2 Menor a 16.92
def TestChiCuadUni(u):
	print("Test de bondad Chi Cuadrado")
	observado=[]
	esperado=100
	c=1.2
	for i in range (10):
		x =0
		for j in range (len(u)):
			if  (c-0.2)<=float(u[j])<=c:
				x+=1
		observado.append(x)
		c+=0.2
	x2=0
	for i in range(len(observado)):
		x2+=(((observado[i]-esperado)**2)/esperado)
	print("X2 = "+ str(x2))

def gamma(k,a):
    x=[]
    for i in range(1, 1000):
        tr=1.0
        for j in range(1,k):
            r = random.random()
            tr=tr*r
        x.append(-(math.log10(tr))/a)
    return x

gam=(gamma(5,20))


def exponencial(ex):
    x = []
    for i in range(1000):
        r = random.random()
        x += [-ex*(np.log(r))]
    return x


expo=(exponencial(5))
#Menor a 16.92
def TestChiCuadExp(u):
    print("Test de bondad Chi Cuadrado")
    observado=[]
    esperado=[]
    c=0.3
    for i in range (9):
        x =0
        for j in range (len(u)):
             if  (c-0.3)<=float(u[j])<=c:
                x+=1
        observado.append(x)
        esperado.append(1000*((1-(math.e)**(-(1/5)*c))-(1-(math.e)**(-(1/5)*(c-0.3)))))
        c+=0.3
    observado.append(1000-sum(observado))
    esperado.append(1000*((math.e)**(-(1/5)*(c-0.3))))
    x2=0
    for i in range(len(observado)):
        x2+=(((observado[i]-esperado[i])**2)/esperado[i])
    print(sum(observado))
    print(sum(esperado))
    print(observado)
    print(esperado)
    print(x2)

def normal(ex,stdx):
    x=[]
    for i in range(1000):
        sum = 0.0
        for j in range (12):
            r=random.random()
            sum += r
        x+=[stdx*(sum-6.0)+ex]
    return x
nor=normal(2.35,30)

#X2 menor a 16.92
def TestChiCuadNormal(u):
    print("Test de bondad Chi Cuadrado")
    observado = []
    esperado = []
    a1=0
    a2=0
    c =-80
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if (c-20) <= float(u[j]) <= c:
                x += 1
        observado.append(x)
        a1+=(c-10)*x
        a2+=((c-10)**2)*x
        c +=20
    a1=a1/1000
    a2=a2/1000
    print(a2)
    print(a1)
    desviacion=math.sqrt(a2-a1**2)
    media=a1
    c=-80
    esperado=[]
    for i in range(10):
        esperado.append (1000*(norm.cdf((c-media)/desviacion)-norm.cdf(((c-20)-media)/desviacion)))
        c+=20
    x2 = 0
    for i in range(len(observado)):
        x2 += (((observado[i]-esperado[i])**2)/esperado[i])
    print(x2)

def poison (lamb):
    x = []
    for i in range(1000):
        cont=0
        tr=1
        b=0
        while(tr-b >= 0):
            b = math.exp(-lamb)
            r = random.random()
            tr=tr*r
            if(tr-b >= 0):
                cont+=1
        x.append(cont)
    return x
poi=poison(50)

def TestChiCuadPoisson(u):
    print("Test de bondad Chi Cuadrado")
    observado = []
    esperado = []
    X=scipy.stats.poisson(50)
    c =26
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if (c-6) <= float(u[j]) < c:
                x += 1
        observado.append(x)
        total=sum(X.pmf(k) for k in range (c)) -sum(X.pmf(m) for m in range (c-6))
        #print(total)
        #print(total)
        esperado.append(1000*total)
        c +=6 
    x2 = 0
    for i in range(len(observado)):
        x2 += (((observado[i]-esperado[i])**2)/esperado[i])
    #print(sum(esperado))
    #print(sum(observado))
    #print(esperado)
    #print(observado)
    print(x2)

def binomial (n,p):
    x=[]
    for i in range(1000):
        y=0.0
        for j in range(1,n):
            r = random.random()
            if (r-p) <0:
                y+=1.0
        x.append(y)
    return x


bino=binomial(1000,0.4)

#Test chi cuad para binomial x2<16.92
def TestChiCuadBinomial(u):
    print("Test de bondad Chi Cuadrado")
    observado = []
    esperado = []
    X=scipy.stats.binom(1000,0.4)
    c =354
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if (c-14) <= float(u[j]) < c:
                x += 1
        observado.append(x)
        total=sum(X.pmf(k) for k in range (c)) -sum(X.pmf(m) for m in range (c-14))
        #print(total)
        esperado.append(1000*total)
        c +=14   
    x2 = 0
    for i in range(len(observado)):
        x2 += (((observado[i]-esperado[i])**2)/esperado[i])
    #print(sum(esperado))
    #print(sum(observado))
    #print(esperado)
    #print(observado)
    print(x2)


def empirica():
    x=[]
    p=[0.273,0.037,0.195,0.009,0.124,0.058,0.062,0.151,0.047,0.044]
    for i in range(1000):
        r=random.random()
        a=0
        for i in p:
          a+=i
          if (r<=a):
            break
        x.append(a)
    return x

empi=empirica()

def TestChiCuadEmpirica(u):
    print("Test de bondad Chi Cuadrado")
    observado = []
    esperado = []
    X=scipy.stats.binom(1000,0.4)
    c =354
    for i in range(10):
        x = 0
        for j in range(len(u)):
            if (c-14) <= float(u[j]) < c:
                x += 1
        observado.append(x)
        total=sum(X.pmf(k) for k in range (c)) -sum(X.pmf(m) for m in range (c-14))
        #print(total)
        esperado.append(1000*total)
        c +=14   
    x2 = 0
    for i in range(len(observado)):
        x2 += (((observado[i]-esperado[i])**2)/esperado[i])
    #print(sum(esperado))
    #print(sum(observado))
    #print(esperado)
    #print(observado)
    print(x2)

def pascal(k,q):
    nx = []
    for i in range(1000):
        tr = 1
        qr = math.log10(q)
        u = generadorRandu()
        for j in range(k):
            r = random.random()
            tr *= u[j]
        x = math.log10(tr)/qr
        nx += [x]
    return nx
    
pas=pascal(5,200)

def hipergeometrica(tn,ns,p):
    x=[]
    for i in range(1000):
        y=0.0
        for j in range(1,ns):
            r = random.random()
            if(r-p)>0:
                s=0.0
            else:
                s=1.0
                y+=1.0
            p=(tn*p-s)/(tn-1.0)
            tn-=1.0
        x.append(y)
    return x

hipergeo=hipergeometrica(5000000,500,0.4)

def graficar(u,g,e,n,p,b,em,pas,hipergeo):
 plt.title("uniforme")
 plt.hist(u)
 plt.show()
 plt.title("gamma")
 plt.hist(g,25,histtype="stepfilled", alpha=.7,linewidth=5, color='r')
 plt.show()
 plt.title("exponencial")
 plt.hist(e, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='g')
 plt.show()
 plt.title("normal")
 plt.hist(n, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='y')
 plt.show()
 plt.title("poisson")
 plt.hist(p, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='orange')
 plt.show()
 plt.title("binomial")
 plt.hist(b, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='black')
 plt.show()
 plt.title("empirica")
 plt.hist(em, 25, histtype="stepfilled", alpha=.7, linewidth=5,color='violet')
 plt.show()
 plt.title("pascal")
 plt.hist(pas, 25, histtype="stepfilled", alpha=.7, linewidth=5,   color='cyan')
 plt.show()
 plt.title("hipergeometrica")
 plt.hist(hipergeo, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='chocolate')
 plt.show()


graficar(uni,gam,expo,nor,poi,bino,empi,pas,hipergeo)
#TestChiCuadUni(uni)
#TestChiCuadExp(expo)
#TestChiCuadNormal(nor)
#TestChiCuadBinomial(bino)
#TestChiCuadPoisson(poi)
