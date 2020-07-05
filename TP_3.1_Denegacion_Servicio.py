import math
import random
import matplotlib.pyplot as plt
import numpy as np
import os





def timing():

    global min_time_next_event
    global time
    global next_event_type
    global min_time_next_event
    global time_next_event
    global num_events


    min_time_next_event=1*10**(29)
    next_event_type=0
    for i in range(num_events):
        if(time_next_event[i]<min_time_next_event):
            min_time_next_event=time_next_event[i]
            next_event_type=i+1
    #if(next_event_type==1):
     #   print("la lista de eventos esta vacia"+str(time))

    time=min_time_next_event


def arrive():
    global server_status
    global time_next_event
    global mean_interarrival
    global num_in_q
    global Q_limit
    global delay
    global total_of_delays
    global num_custs_delayed
    global time_arrival
    global time
    global mean_service
    global num_clientes_sistema
    global tiempo_2
    global area_num_in_q_total
    global utilizacion_servidor_total
    global total_denegados

    #time_next_event.pop(0)
    time_next_event[0] = time+expon(mean_interarrival)

    #time_next_event.insert(0,float(time+expon(mean_interarrival)))
    if(server_status==1):
        if(num_in_q>=Q_limit):
            total_denegados+=1
            num_in_q-=1
            
        time_arrival.insert(num_in_q,time)
        num_in_q += 1
        
        num_clientes_sistema.append(num_in_q+1)

        area_num_in_q_total.append(num_in_q)

        
    else:
        delay=0
        total_of_delays+=delay
        num_custs_delayed+=1

        num_clientes_sistema.append(num_in_q)
        
        area_num_in_q_total.append(0)
        
        server_status=1
        time_next_event[1]=time+expon(mean_service)

        tiempo_2.append(time_next_event[1]-time)

    



    time_global.append(time)

        #tiempo_llegada=time
    #   time_next_event.insert(1,float(time+expon(mean_service)))
    #num_clientes_sistema.append(num_in_q)

def depart():
    global delay
    global server_status
    global num_in_q
    global time_next_event
    global num_custs_delayed
    global total_of_delays
    global time_arrival
    global time
    global num_clientes_sistema
    global tiempo_2
    global area_num_in_q_total
    global ListaDemoras
    global utilizacion_servidor_total


    if(num_in_q == 0):

        server_status=0
        #time_next_event[1]=1*10**30
        time_next_event[1] =float(math.inf)

        #Media demoras
        ListaDemoras.append(0)
        num_clientes_sistema.append(num_in_q)
        area_num_in_q_total.append(0)

        
        

    else:

        num_in_q-=1
        delay=time - time_arrival[0]
        
        #media de demoras
        ListaDemoras.append(delay)
        
        num_clientes_sistema.append(num_in_q)

        total_of_delays+=delay
        num_custs_delayed+=1



        time_next_event[1]=float(time+expon(mean_service))
        
        tiempo_2.append(time_next_event[1]-time_arrival[0])

        for i in range(num_in_q):
            time_arrival[i]=time_arrival[i+1]

        area_num_in_q_total.append(num_in_q-1)


    time_global.append(time)
    



    #num_clientes_sistema.append(num_in_q)

def report():
    global total_of_delays
    global num_custs_delayed
    global area_num_in_q
    global time
    global area_server_status
    global num_delays_required
    global mean_service
    global num_clientes_sistema
    global tiempo_2
    global prob_n_clientes_cola

    print("Promedio de clientes en el sistema: "+str((sum(num_clientes_sistema))/len(num_clientes_sistema)))

    print("Promedio de clientes en cola: "+str(area_num_in_q/time))

    print("Tiempo Promedio en el sistema: "+str(sum(tiempo_2)/num_delays_required))

    print("Tiempo promedio en cola : "+ str(total_of_delays/num_delays_required))

    print("Utilizacion del servidor: "+str(area_server_status/time))

    print("Tiempo de fin de simulacion"+ str(time))

    prob_n_clientes_cola = ((1-(1/mean_interarrival)/(1/mean_service))*((1/mean_interarrival)/(1/mean_service))**int(numero_clientes_cola))
    print("La probabilidad de que haya: " + str(numero_clientes_cola)+" clientes en cola es de:"+str(prob_n_clientes_cola))


def update_time_avg_state():

    global time_last_event
    global time
    global area_num_in_q
    global num_in_q
    global time_since_last_event
    global area_server_status
    global server_status
    global utilizacion_servidor_total

    time_since_last_event=time-time_last_event
    time_last_event=time

    area_num_in_q +=num_in_q*time_since_last_event

    #print(time_since_last_event)
    #Creo que lo que pasa es que me multiplica por 0 siempre que no haya otro numero
    area_server_status+=server_status*time_since_last_event

    utilizacion_servidor_total.append(area_server_status/time)



def expon(mean):

    u=random.random()
    return (-mean*math.log(u))


def inicializar():
    global time
    global server_status
    global num_in_q
    global time_last_event
    global num_custs_delayed
    global total_of_delays
    global area_server_status
    global time_next_event
    global area_num_in_q
    global time_arrival
    global num_clientes_sistema
    global tiempo_llegada 
    global tiempo_2
    global time_global
    global area_num_in_q_total
    global ListaDemoras
    global utilizacion_servidor_total



    time_global=[]

    time = 0
    
    area_num_in_q_total = []

    num_clientes_sistema=[]

    ListaDemoras=[]

    utilizacion_servidor_total=[]


    tiempo_llegada=0
    tiempo_2=[]

    server_status = 0
    num_in_q = 0
    time_last_event = 0

    num_custs_delayed = 0
    total_of_delays = 0
    area_num_in_q = 0
    area_server_status = 0

    time_next_event = []
    time_next_event.insert(0, float(time+expon(mean_interarrival)))
   # time_next_event.insert(1, float(1*10**(30)))
    time_next_event.insert(1,float(math.inf))
    time_arrival=[]


mean_interarrival = float( input("Media del arribo: "))
mean_service=float(input("Media del servicio: "))
num_delays_required = float(input("Numero de clientes total: "))

def MainProgram():
#Ingresa media, media de servicio, tiempo de finalizacion
    global num_events
    global mean_interarrival
    global mean_service
    global num_delays_required
    global numero_clientes_cola
    global num_custs_delayed
    global next_event_type
    global total_denegados
    global total_denegados_gral

    total_denegados=0
    num_events=2
    #mean_interarrival = float( input("media del arribo: "))
    #mean_service=float(input("media del servicio: "))
    #num_delays_required = float(input("num delays requiered: "))



    #Inicializa

    inicializar()



    #continua 
    #while(num_custs_delayed<num_delays_required):
    #arribos=0
    #departos=0

    while(num_custs_delayed < num_delays_required):
        timing()
        update_time_avg_state()

        if(next_event_type==1):
            arrive()
            #arribos+=1

            
        elif(next_event_type==2):
            depart()
    
    total_denegados_gral+=total_denegados
            #departos+=1
    #report()








def PastelProbabilidadClienteDenegadoCola():
    global total_denegados
    global Q_limit
    global total_denegados_gral
    porcentajes = (total_denegados_gral/1000,1-total_denegados_gral/1000 )
    nombres = ("Probabilidad que sea denegado un cliente con una cola de capacidad de: " + str(Q_limit),"Probabilidad que NO sea denegado un cliente con uan cola de capacidad de: " + str(Q_limit))
    plt.pie(porcentajes, labels=nombres, autopct="%0.1f %%")

    plt.savefig("Prob_n_clientes_denegados_75.png")


#GraficasPromClientesSistema(num_clientes_sistema) #Graficas clientes-sistema
#GraficasPromClientesSistema(area_num_in_q_total) # Grafica clientes -Cola
#GraficasTiempoClientesSistema(tiempo_2)     #Grafica tiempo cliente en el sistema , en el x el numero de cliente, en el y los tiempos
#GraficasTiempoClientesSistema(ListaDemoras) #Grafica tiempo cliente en cola , en el x el numero de cliente, en el y los tiempos
#GraficasPromClientesSistema(utilizacion_servidor_total) #Grafica utilizacion del servidor
#PastelUtilizacionServidor() #Grafica pastel servidor



global total_denegados
global Q_limit
global total_denegados_gral

total_denegados_gral=0

Q_limit=int(input("Ingrese el tamaño maximo de la cola"))

for i in range(1000):
    MainProgram()
total_denegados_gral=total_denegados_gral/1000
print("Cantidad de personas denegadas promedio:  "+str(total_denegados_gral))
PastelProbabilidadClienteDenegadoCola()
plt.show()
    



#print(arribos)
#print(departos)
#print(num_custs_delayed)
#print(len(time_next_event))


#IMPORTANTE, EN LA CALCULADORA UTILIZAR LA INVERSA DE LAS MEDIAS.

#IMPORTANTE 2: Utilizaremos media de servicio =1
# media de arribo: 4,2,4/3,1, 0.8 las 

