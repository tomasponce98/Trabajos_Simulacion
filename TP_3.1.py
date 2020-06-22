import math
import random
import matplotlib.pyplot as plt

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

    #time_next_event.pop(0)
    time_next_event[0] = time+expon(mean_interarrival)
    #time_next_event.insert(0,float(time+expon(mean_interarrival)))
    if(server_status==1):
        if(num_in_q>Q_limit):
            print("se rompio la cola")
            
        time_arrival.insert(num_in_q,time)
        num_in_q += 1
    else:
        delay=0
        total_of_delays+=delay
        num_custs_delayed+=1
        server_status=1
        time_next_event[1]=time+expon(mean_service)
#        time_next_event.insert(1,float(time+expon(mean_service)))

def depart():
    global delay
    global server_status
    global num_in_q
    global time_next_event
    global num_custs_delayed
    global total_of_delays
    global time_arrival
    global time
    
    if(num_in_q==0):

        server_status=0
        #time_next_event[1]=1*10**30
        time_next_event[1] =float(math.inf)
    else:
        
        num_in_q-=1
        delay=time - time_arrival[0]
        #print(delay)
        total_of_delays+=delay
        num_custs_delayed+=1
        time_next_event[1]=float(time+expon(mean_service))
        for i in range(num_in_q):
            time_arrival[i]=time_arrival[i+1]

def report():
    global total_of_delays
    global num_custs_delayed
    global area_num_in_q
    global time
    global area_server_status
    global num_delays_required

    print("Average delay in queue: "+ str(total_of_delays/num_delays_required))
    print("Average number in queue: "+str(area_num_in_q/time))
    print("Server utilization: "+str(area_server_status/time))
    print("Time simulation ended"+ str(time))

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

    time = 0
    
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
        #departos+=1
report()
#print(arribos)
#print(departos)
#print(num_custs_delayed)
#print(len(time_next_event))


#IMPORTANTE, EN LA CALCULADORA UTILIZAR LA INVERSA DE LAS MEDIAS.


    
