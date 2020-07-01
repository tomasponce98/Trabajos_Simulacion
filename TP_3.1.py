import math
import random
import matplotlib.pyplot as plt
import numpy as np

# def mm1(numero_clientes):
#     clientes=[]
#     tll=[]
#     te=[]
#     tser=[]
#     tocio=[]
#     tsal=[]
#     num_clientes=numero_clientes
#     i=0
#     while(i<num_clientes):
#         if(i==0):
#             clientes.append(i)
#             tll.append(0)
#             te.append(0)
#             tser.append(random.random())
#             tocio.append(0)
#             tsal.append(tll[0]+te[0]+tser[0]+random.random())
#         if(i>=1):
#            clientes.append(i)
#            tll.append(tll[i-1]+random.random())
#            te.append(max(tsal[i-1],tll[i])-tll[i])
#            tser.append(random.random())
#            tocio.append(max(tsal[i-1], tll[i])-tll[i-1])
#            tsal.append(tll[i]+te[i]+tser[i])
#         i+=1
#     for i in range(len(clientes)):
#         print("Cliente: "+str(clientes[i])+", Tiempo de llegada: "+str(tll[i])+
#           ", Tiempo de espera:  "+str(te[i])+", Tiempo de servicio: "+str(tser[i])+
#           " , Tiempo de salida:  "+str(tsal[i]))
#     plt.plot(clientes, tll, label="tiempod de de llegada", color="r")
#     plt.plot(clientes, te, label="tiempo de espera",color="g")
#     plt.plot(clientes, tser, label="tiempo de servicio", color="b")
#     plt.plot(clientes, tsal, label="tiempo de salida",color="y")
#     plt.show()
# mm1(5)

#next_event_type,num_cust_delayed,num_delays_required,num_events,num_in_q, server_status=0
#area_num_in_q,area_server_status,mean_interarrival,_mean_service,time,time_arrival,time_last_event,time_next_event,total_of_delays=0



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


    #time_next_event.pop(0)
    time_next_event[0] = time+expon(mean_interarrival)
    #time_next_event.insert(0,float(time+expon(mean_interarrival)))
    if(server_status==1):
        if(num_in_q>Q_limit):
            print("se rompio la cola")
            
        time_arrival.insert(num_in_q,time)
        num_in_q += 1
        
        num_clientes_sistema.append(num_in_q+1)
        
    else:
        delay=0
        total_of_delays+=delay
        num_custs_delayed+=1

        num_clientes_sistema.append(num_in_q)

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

    if(num_in_q==0):

        server_status=0
        #time_next_event[1]=1*10**30
        time_next_event[1] =float(math.inf)

        #Media demoras
        #EstadisticosDemoras(0)
        num_clientes_sistema.append(num_in_q)
        
        

    else:

        num_in_q-=1
        delay=time - time_arrival[0]
        
        #media de demoras
        #EstadisticosDemoras(delay)
        
        num_clientes_sistema.append(num_in_q)

        total_of_delays+=delay
        num_custs_delayed+=1



        time_next_event[1]=float(time+expon(mean_service))
        
        tiempo_2.append(time_next_event[1]-time_arrival[0])

        for i in range(num_in_q):
            time_arrival[i]=time_arrival[i+1]

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

    time_since_last_event=time-time_last_event
    time_last_event=time

    area_num_in_q +=num_in_q*time_since_last_event
    #print(time_since_last_event)
    #Creo que lo que pasa es que me multiplica por 0 siempre que no haya otro numero
    area_server_status+=server_status*time_since_last_event

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

    time_global=[]

    time = 0
    
    num_clientes_sistema=[]

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




#Ingresa media, media de servicio, tiempo de finalizacion
Q_limit=100
num_events=2
mean_interarrival = float( input("media del arribo: "))
mean_service=float(input("media del servicio: "))
num_delays_required = float(input("num delays requiered: "))

numero_clientes_cola=input("Cuantos clientes en cola habra?")


#Inicializa

inicializar()

# Estadisticos que utilizaremos
ListaDemoras=[]
ListaMediaDemoras=[]

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
        #departos+=1
report()


def EstadisticosDemoras(delay):
    ListaDemoras.append(delay)
    ListaMediaDemoras.append(np.mean(ListaDemoras))

def GraficasDemoras():
    global total_of_delays
    global num_delays_required
    plt.figure(1)
    plt.plot(ListaMediaDemoras)
    listaDemoraTotal=[]
    for i in range(len(ListaMediaDemoras)):
        listaDemoraTotal.append(total_of_delays/num_delays_required)
    plt.plot(ListaMediaDemoras)
    plt.plot(listaDemoraTotal)
    plt.show()

def GraficasPromClientesSistema():
    global num_clientes_sistema
    global numero_clientes_cola
    
    listaClientes = []

    acum_clientes_sistema = np.cumsum(num_clientes_sistema)

    num_clientes_sistema_media = []
    for i in range(len(num_clientes_sistema)):
        num_clientes_sistema_media.append(acum_clientes_sistema[i]/(i+1))
        

    num_clientes_sistema_varianza=[]
    num_clientes_sistema_desviacion=[]
    num_clientes_sistema_fr=[]
    contador=0
    k=0

    for i in range(len(num_clientes_sistema)):
        listaClientes.append(num_clientes_sistema[i])
        num_clientes_sistema_varianza.append(np.var(listaClientes))
        num_clientes_sistema_desviacion.append(np.std(listaClientes))
        if(int(listaClientes[i]) == int(numero_clientes_cola)):
            contador+=1
            num_clientes_sistema_fr.append(contador/(i+1))
            k=i
        else:
            num_clientes_sistema_fr.append(contador/(k+1))

    media_cli_sistema=[]
    for i in range (len(num_clientes_sistema)):
        media_cli_sistema.append(np.mean(num_clientes_sistema))

    varianza_cli_sistema=[]
    for i in range(len(num_clientes_sistema)):
        varianza_cli_sistema.append(np.var(num_clientes_sistema))

    desviacion_cli_sistema = []
    for i in range(len(num_clientes_sistema)):
        desviacion_cli_sistema.append(np.std(num_clientes_sistema))
    

    
    
   
    plt.plot(time_global, num_clientes_sistema_media)
    plt.plot(time_global,media_cli_sistema)
    plt.show()

    plt.plot(time_global, num_clientes_sistema_varianza)
    plt.plot(time_global,varianza_cli_sistema)
    plt.show()

    plt.plot(time_global, num_clientes_sistema_desviacion)
    plt.plot(time_global,desviacion_cli_sistema)
    plt.show()



    

GraficasPromClientesSistema()


#print(arribos)
#print(departos)
#print(num_custs_delayed)
#print(len(time_next_event))


#IMPORTANTE, EN LA CALCULADORA UTILIZAR LA INVERSA DE LAS MEDIAS.


    
