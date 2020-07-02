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

    #time_next_event.pop(0)
    time_next_event[0] = time+expon(mean_interarrival)

    #time_next_event.insert(0,float(time+expon(mean_interarrival)))
    if(server_status==1):
        if(num_in_q>Q_limit):
            print("se rompio la cola")
            
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


mean_interarrival = float( input("media del arribo: "))
mean_service=float(input("media del servicio: "))
num_delays_required = float(input("num delays requiered: "))

def MainProgram():
#Ingresa media, media de servicio, tiempo de finalizacion
    global Q_limit
    global num_events
    global mean_interarrival
    global mean_service
    global num_delays_required
    global numero_clientes_cola
    global num_custs_delayed
    global next_event_type

    Q_limit=100
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
            #departos+=1
    #report()






def GraficaPromClientesSistemaMedia(arreglo):
    #global num_clientes_sistema
     
    

    global numero_clientes_cola
    global media_gral
    global varianza_gral
    global desvio_gral
    global contador_gral
        
 
    listaClientes = []

    acum_clientes_sistema = np.cumsum(arreglo)

    num_clientes_sistema_media = []
    for i in range(len(arreglo)):
        num_clientes_sistema_media.append(acum_clientes_sistema[i]/(i+1))
            

    

    media_cli_sistema=[]
    for i in range(len(arreglo)):
        media_cli_sistema.append(np.mean(arreglo))

    
    media_gral+=np.mean(arreglo)

    
    plt.figure(1)
    plt.plot(time_global, num_clientes_sistema_media)
    if (contador_gral == 10):
        media_cli_sistema = []
        for i in range(len(arreglo)):
            media_cli_sistema.append(media_gral/10)
        plt.plot(time_global, media_cli_sistema,label="Media esperada de clientes en el sistema")
        plt.legend()
    


def GraficaPromClientesSistemaVarianza(arreglo):

    global numero_clientes_cola
    global media_gral
    global varianza_gral
    global desvio_gral
    global contador_gral

    listaClientes = []


    

    num_clientes_sistema_varianza = []

    for i in range(len(arreglo)):
        listaClientes.append(arreglo[i])
        num_clientes_sistema_varianza.append(np.var(listaClientes))



    varianza_cli_sistema = []
    for i in range(len(arreglo)):
        varianza_cli_sistema.append(np.var(arreglo))


    varianza_gral += np.var(arreglo)

    plt.figure(2)

    plt.plot(time_global, num_clientes_sistema_varianza)
    if (contador_gral == 10):
        varianza_cli_sistema = []
        for i in range(len(arreglo)):
            varianza_cli_sistema.append(varianza_gral/10)
        plt.plot(time_global, varianza_cli_sistema,label="Varianza esperada de clientes ")
        plt.legend()


def GraficaPromClientesSistemaDesvio(arreglo):
    global numero_clientes_cola
    global media_gral
    global varianza_gral
    global desvio_gral
    global contador_gral

    listaClientes = []


 

    num_clientes_sistema_desviacion = []

    for i in range(len(arreglo)):
        listaClientes.append(arreglo[i])
        num_clientes_sistema_desviacion.append(np.std(listaClientes))

 

    desviacion_cli_sistema = []
    for i in range(len(arreglo)):
        desviacion_cli_sistema.append(np.std(arreglo))

    desvio_gral += np.std(arreglo)

    plt.figure(3)
    plt.plot(time_global, num_clientes_sistema_desviacion)

    if (contador_gral == 10):
        desviacion_cli_sistema = []
        for i in range(len(arreglo)):
            desviacion_cli_sistema.append(desvio_gral/10)

        plt.figure(3)
        plt.plot(time_global, desviacion_cli_sistema,label="Desviacion esperada de clientes")
        plt.legend()



    


def GraficasTiempoClientesSistema(arreglo):
    #global num_clientes_sistema

    listaClientes = []

    acum_clientes_sistema = np.cumsum(arreglo)

    num_clientes_sistema_media = []
    for i in range(len(arreglo)):
        num_clientes_sistema_media.append(acum_clientes_sistema[i]/(i+1))

    num_clientes_sistema_varianza = []
    num_clientes_sistema_desviacion = []
    num_clientes_sistema_fr = []
    contador = 0
    k = 0

    for i in range(len(arreglo)):
        listaClientes.append(arreglo[i])
        num_clientes_sistema_varianza.append(np.var(listaClientes))
        num_clientes_sistema_desviacion.append(np.std(listaClientes))
        if(int(listaClientes[i]) == int(numero_clientes_cola)):
            contador += 1
            num_clientes_sistema_fr.append(contador/(i+1))
            k = i
        else:
            num_clientes_sistema_fr.append(contador/(k+1))

    media_cli_sistema = []
    for i in range(len(arreglo)):
        media_cli_sistema.append(np.mean(arreglo))

    varianza_cli_sistema = []
    for i in range(len(arreglo)):
        varianza_cli_sistema.append(np.var(arreglo))

    desviacion_cli_sistema = []
    for i in range(len(arreglo)):
        desviacion_cli_sistema.append(np.std(arreglo))

    plt.plot(num_clientes_sistema_media)
    plt.plot(media_cli_sistema)
    plt.show()

    plt.plot(num_clientes_sistema_varianza)
    plt.plot(varianza_cli_sistema)
    plt.show()

    plt.plot(num_clientes_sistema_desviacion)
    plt.plot(desviacion_cli_sistema)
    plt.show()

def PastelUtilizacionServidor():
    global area_server_status
    global time
    porcentajes = ((area_server_status/time)*100, (1-area_server_status/time)*100)
    nombres=("Porcentaje utilizado del servidor","Porcentaje no utilizado del servidor")
    plt.pie(porcentajes, labels=nombres, autopct="%0.1f %%")
    plt.show()


#GraficasPromClientesSistema(num_clientes_sistema) #Graficas clientes-sistema
#GraficasPromClientesSistema(area_num_in_q_total) # Grafica clientes -Cola
#GraficasTiempoClientesSistema(tiempo_2)     #Grafica tiempo cliente en el sistema , en el x el numero de cliente, en el y los tiempos
#GraficasTiempoClientesSistema(ListaDemoras) #Grafica tiempo cliente en cola , en el x el numero de cliente, en el y los tiempos
#GraficasPromClientesSistema(utilizacion_servidor_total) #Grafica utilizacion del servidor
#PastelUtilizacionServidor() #Grafica pastel servidor

def menu():
    print(" ")
    print("MENÚ PRINCIPAL - Seleccione una opción")
    print("1 - Promedio de clientes en el sistema")
    print("2 - Promedio de clientes en cola")
    print("3 - Tiempo promedio en sistema")
    print("4 - Tiempo promedio en cola")
    print("5 - Utilización del servidor")
    print("6 - Probabilidad de n cliente en cola")
    print("0 - Salir")


while True:
    os.system('cls')    

    menu()

    opcionMenu = input("Ingrese su opcion:  ")
    print(" ")

    if opcionMenu == "1":
        contador_gral=0
        media_gral = 0
        varianza_gral=0
        desvio_gral=0
        for i in range(10):
            contador_gral+=1
            MainProgram()
            GraficaPromClientesSistemaMedia(num_clientes_sistema)
            plt.title("Media de clientes en el sistema")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Media de clientes")

            GraficaPromClientesSistemaVarianza(num_clientes_sistema)
            plt.title("Varianza de los clientes en el sistema")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Varianza de clientes")
            
            GraficaPromClientesSistemaDesvio(num_clientes_sistema)
            plt.title("Desviacion de los clientes en el sistema")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Desviacion de clientes")
        plt.show()
        #plt.show()
        
        input("Pulsa una tecla para continuar")
    elif opcionMenu == "2":
        GraficaPromClientesSistemaMedia(area_num_in_q_total)
        input("Pulsa una tecla para continuar")
    elif opcionMenu == "3":
        GraficaPromClientesSistemaMedia(tiempo_2)
        input("Pulsa una tecla para continuar")
    elif opcionMenu == "4":
        GraficaPromClientesSistemaMedia(ListaDemoras)
        input("Pulsa una tecla para continuar")
    elif opcionMenu == "5":
        GraficaPromClientesSistemaMedia(utilizacion_servidor_total)
        PastelUtilizacionServidor()

        input("Pulsa una tecla para continuar")

    elif opcionMenu == "6":
        numero_clientes_cola = input("Cuantos clientes en cola habra?")

        prob_n_clientes_cola = ((1-(1/mean_interarrival)/(1/mean_service)) *((1/mean_interarrival)/(1/mean_service))**int(numero_clientes_cola))
        print("La probabilidad de que haya: " + str(numero_clientes_cola) +" clientes en cola es de:"+str(prob_n_clientes_cola))
        input("Pulsa una tecla para continuar")
    elif opcionMenu == "0":
        break
    else:
        print(" ")
        input("No has pulsado ninguna opción correcta... \n Pulsa una tecla para continuar")





#print(arribos)
#print(departos)
#print(num_custs_delayed)
#print(len(time_next_event))


#IMPORTANTE, EN LA CALCULADORA UTILIZAR LA INVERSA DE LAS MEDIAS.


    
