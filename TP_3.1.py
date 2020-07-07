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

    time_next_event[0] = time+expon(mean_interarrival)

    if(server_status==1):

            
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
        time_next_event[1] =float(math.inf)

        ListaDemoras.append(0)
        num_clientes_sistema.append(num_in_q)
        area_num_in_q_total.append(0)

        
        

    else:

        num_in_q-=1
        delay=time - time_arrival[0]
        
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
    time_next_event.insert(1,float(math.inf))
    time_arrival=[]


mean_interarrival = float( input("Media del arribo: "))
mean_service=float(input("Media del servicio: "))
num_delays_required = float(input("Numero de clientes total: "))

def MainProgram():
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


    inicializar()





    while(num_custs_delayed < num_delays_required):
        timing()
        update_time_avg_state()

        if(next_event_type==1):
            arrive()

            
        elif(next_event_type==2):
            depart()










def GraficaPromClientesSistemaMedia(arreglo):
    #global num_clientes_sistema
    global media_de_las_medias

    global numero_clientes_cola
    global media_gral
    global varianza_gral
    global desvio_gral
    global contador_gral
    global media_total_utlizacion_servidor
    global media_de_las_medias
    global tiempo_a_utilizar

  

    acum_clientes_sistema = np.cumsum(arreglo)

    num_clientes_sistema_media = []
    for i in range(len(arreglo)):
        num_clientes_sistema_media.append(acum_clientes_sistema[i]/(i+1))

    media_cli_sistema = []
    for i in range(len(arreglo)):
        media_cli_sistema.append(np.mean(arreglo))

    if (contador_gral == 1):
        
        for i in range(len(num_clientes_sistema_media)):
            media_de_las_medias.append(num_clientes_sistema_media[i]/10)
        tiempo_a_utilizar=time_global
    else:
        if(len(media_de_las_medias) >= len(num_clientes_sistema_media)):
            longitud = len(num_clientes_sistema_media)
        else:
            longitud=len(media_de_las_medias)
        for i in range(longitud):
            media_de_las_medias[i] = media_de_las_medias[i]+(num_clientes_sistema_media[i])/10

    media_gral += np.mean(arreglo)

    plt.figure(1)
    plt.plot(time_global, num_clientes_sistema_media, color="orange")

   
    if (contador_gral == 10):

        if (opcionMenu == "5"):
            media_gral=media_gral/10
            plt.plot(tiempo_a_utilizar, media_de_las_medias,label="Media esperada de utilizacion del servidor en el sistema", color="blue")
        else:
            plt.plot(tiempo_a_utilizar, media_de_las_medias,label="Media esperada de clientes en el sistema", color="blue")
        plt.legend()
    plt.savefig("Utilizacion_Servidor_Media.png")



def GraficaPromTiempoSistemaMedia(arreglo):
    #global num_clientes_sistema

    global numero_clientes_cola
    global media_gral
    global varianza_gral
    global desvio_gral
    global contador_gral
    global media_de_las_medias

    acum_clientes_sistema = np.cumsum(arreglo)

    num_clientes_sistema_media = []
    for i in range(len(arreglo)):
        num_clientes_sistema_media.append(acum_clientes_sistema[i]/(i+1))

    media_cli_sistema = []
    for i in range(len(arreglo)):
        media_cli_sistema.append(np.mean(arreglo))

    media_gral += np.mean(arreglo)

    if (contador_gral == 1):
        for i in range(len(num_clientes_sistema_media)):
            media_de_las_medias.append(num_clientes_sistema_media[i]/10)
    else:
        for i in range(len(media_de_las_medias)):
            media_de_las_medias[i] = media_de_las_medias[i] + (num_clientes_sistema_media[i])/10

    plt.figure(1)
    plt.plot(num_clientes_sistema_media,color="black")
    if (contador_gral == 10):
        plt.plot(media_de_las_medias, label="Media esperada de tiempo", color="red")
        plt.legend()
    plt.savefig("Tiempos_Cola_Media.png")

    


def GraficaPromClientesSistemaVarianza(arreglo):

    global numero_clientes_cola
    global media_gral
    global varianza_gral
    global desvio_gral
    global contador_gral
    global varianza_de_las_varianzas
    global tiempo_a_utilizar

    listaClientes = []


    

    num_clientes_sistema_varianza = []

    for i in range(len(arreglo)):
        listaClientes.append(arreglo[i])
        num_clientes_sistema_varianza.append(np.var(listaClientes))
    
    if (contador_gral == 1):
        for i in range(len(num_clientes_sistema_varianza)):
            varianza_de_las_varianzas.append(num_clientes_sistema_varianza[i]/10)
        tiempo_a_utilizar=time_global
    else:

        if(len(varianza_de_las_varianzas) >= len(num_clientes_sistema_varianza)):
            longitud = len(num_clientes_sistema_varianza)
        else:
            longitud = len(varianza_de_las_varianzas)
        for i in range(longitud):
            varianza_de_las_varianzas[i] = varianza_de_las_varianzas[i]+(num_clientes_sistema_varianza[i])/10



    

    plt.figure(2)

    plt.plot(time_global, num_clientes_sistema_varianza, color="orange")
    if (contador_gral == 10):
     
        
        if (opcionMenu=="5"):
            plt.plot(tiempo_a_utilizar, varianza_de_las_varianzas,label="Varianza esperada de utilización del servidor ", color="blue")
        else:
            plt.plot(tiempo_a_utilizar, varianza_de_las_varianzas,label="Varianza esperada de clientes ",color="blue")
        plt.legend()

    plt.savefig("Utilizacion_Servidor_Varianza.png")



def GraficaPromTiempoSistemaVarianza(arreglo):

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

    if (contador_gral == 1):
        for i in range(len(num_clientes_sistema_varianza)):
            varianza_de_las_varianzas.append(num_clientes_sistema_varianza[i]/10)
    else:
        for i in range(len(varianza_de_las_varianzas)):
            varianza_de_las_varianzas[i] = varianza_de_las_varianzas[i] +(num_clientes_sistema_varianza[i])/10

    plt.figure(2)

    plt.plot(num_clientes_sistema_varianza,color="black")
    if (contador_gral == 10):
        plt.plot(varianza_de_las_varianzas,label="Varianza esperada de tiempo ",color="red")
        plt.legend()

    plt.savefig("Tiempos_Cola_Varianza.png")




def GraficaPromClientesSistemaDesvio(arreglo):
    global numero_clientes_cola
    global media_gral
    global varianza_gral
    global desvio_gral
    global contador_gral
    global desvio_de__desvios
    global tiempo_a_utilizar
    
    listaClientes = []


 

    num_clientes_sistema_desviacion = []

    for i in range(len(arreglo)):
        listaClientes.append(arreglo[i])
        num_clientes_sistema_desviacion.append(np.std(listaClientes))

 

    desviacion_cli_sistema = []
    for i in range(len(arreglo)):
        desviacion_cli_sistema.append(np.std(arreglo))

    if (contador_gral == 1):
        for i in range(len(num_clientes_sistema_desviacion)):
            desvio_de__desvios.append(num_clientes_sistema_desviacion[i]/10)
        tiempo_a_utilizar=time_global
    else:

        if(len(desvio_de__desvios) >= len(num_clientes_sistema_desviacion)):
            longitud = len(num_clientes_sistema_desviacion)
        else:
            longitud = len(desvio_de__desvios)

        for i in range(longitud):
            desvio_de__desvios[i] = desvio_de__desvios[i] +(num_clientes_sistema_desviacion[i])/10


    plt.figure(3)
    plt.plot(time_global, num_clientes_sistema_desviacion,color="orange")

    if (contador_gral == 10):
        

        plt.figure(3)
        if(opcionMenu=="5"):
            plt.plot(tiempo_a_utilizar, desvio_de__desvios,label="Desviacion esperada de utilización del servidor",color="blue")
        else:
            plt.plot(tiempo_a_utilizar, desvio_de__desvios,label="Desviacion esperada de clientes",color="blue")
        plt.legend()

    plt.savefig("Utilizacion_Servidor_Desvio.png")



def GraficaPromTiempoSistemaDesvio(arreglo):
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


    if (contador_gral == 1):
        for i in range(len(num_clientes_sistema_desviacion)):
            desvio_de__desvios.append(num_clientes_sistema_desviacion[i]/10)
    else:
        for i in range(len(desvio_de__desvios)):
            desvio_de__desvios[i] = desvio_de__desvios[i] +  (num_clientes_sistema_desviacion[i])/10

    plt.figure(3)
    plt.plot(num_clientes_sistema_desviacion,color="black")

    if (contador_gral == 10):
        plt.figure(3)
        plt.plot(desvio_de__desvios,label="Desviacion esperada de tiempos",color="red")
        plt.legend()

    plt.savefig("Tiempos_Cola_Desvio.png")








    



def PastelUtilizacionServidor():
    global area_server_status
    global time
    global media_gral
    porcentajes = ((media_gral)*100, (1-media_gral)*100)
    nombres=("Porcentaje utilizado del servidor","Porcentaje no utilizado del servidor")
    plt.pie(porcentajes, labels=nombres, autopct="%0.1f %%")

    plt.savefig("Utilizacion_servidor.png")



def PastelProbabilidadClienteCola():
    global area_server_status
    global time
    global media_total_utlizacion_servidor
    global prob_n_clientes_cola
    global numero_clientes_cola
    porcentajes = ((prob_n_clientes_cola)*100, (1-prob_n_clientes_cola)*100)
    nombres = ("Probabilidad que haya: " + str(numero_clientes_cola)+" clientes en cola",
               "Probabilidad que NO haya: " + str(numero_clientes_cola)+" clientes en cola")
    plt.pie(porcentajes, labels=nombres, autopct="%0.1f %%")

    plt.savefig("Prob_n_clientes.png")


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
    print("6 - Probabilidad de n clientes en cola")
    print("0 - Salir")


while True:
    global opcionMenu
    os.system('cls')    

    menu()

    opcionMenu = input("Ingrese su opcion:  ")
    print(" ")

    if opcionMenu == "1":
        contador_gral=0
        media_gral = 0
        varianza_gral=0
        desvio_gral=0
        media_de_las_medias=[]
        varianza_de_las_varianzas=[]
        desvio_de__desvios=[]
        for i in range(10):
            contador_gral+=1
            MainProgram()
            GraficaPromClientesSistemaMedia(num_clientes_sistema)
            plt.title("Media de clientes en el sistema")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Valor de la media de clientes en sistema")

            GraficaPromClientesSistemaVarianza(num_clientes_sistema)
            plt.title("Varianza de los clientes en el sistema")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Valor de la varianza de clientes en sistema")
            
            GraficaPromClientesSistemaDesvio(num_clientes_sistema)
            plt.title("Desviacion de los clientes en el sistema")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Valor de la desviacion de clientes en sistema")
        plt.show()
        
        input("Pulsa una tecla para continuar")
    elif opcionMenu == "2":
        contador_gral = 0
        media_gral = 0
        varianza_gral = 0
        desvio_gral = 0
        media_de_las_medias = []
        varianza_de_las_varianzas = []
        desvio_de__desvios = []
        for i in range(10):

            contador_gral += 1
            MainProgram()
            GraficaPromClientesSistemaMedia(area_num_in_q_total)
            plt.title("Media de clientes en cola")
            plt.xlabel("Tiempo(segundos)") 
            plt.ylabel("Valor de la media de clientes en cola")

            GraficaPromClientesSistemaVarianza(area_num_in_q_total)
            plt.title("Varianza de los clientes en cola")
            plt.xlabel("Tiempo(segundos)")  
            plt.ylabel("Valor de la varianza de clientes en cola")

            GraficaPromClientesSistemaDesvio(area_num_in_q_total)
            plt.title("Desviacion de los clientes en cola")
            plt.xlabel("Tiempo(segundos)")  
            plt.ylabel("Valor de la desviacion de clientes en cola")
        plt.show()


        input("Pulsa una tecla para continuar")


    elif opcionMenu == "3":
        
        contador_gral = 0
        media_gral = 0
        varianza_gral=0
        desvio_gral=0
        media_de_las_medias = []
        varianza_de_las_varianzas = []
        desvio_de__desvios = []
        for i in range(10):
            contador_gral+=1
            MainProgram()
            GraficaPromTiempoSistemaMedia(tiempo_2)
            plt.title("Media de los tiempos en el sistema")
            plt.xlabel("Numero de Cliente")  # título del eje x
            plt.ylabel("Valor de la media de tiempo en sistema")

            GraficaPromTiempoSistemaVarianza(tiempo_2)
            plt.title("Varianza de los tiempos en el sistema")
            plt.xlabel("Numero de Cliente")  # título del eje x
            plt.ylabel("Valor de la varianza de tiempo en sistema")
            
            GraficaPromTiempoSistemaDesvio(tiempo_2)
            plt.title("Desviacion de los tiempos en el sistema")
            plt.xlabel("Numero de Cliente")  # título del eje x
            plt.ylabel("Valor de la desviación de tiempo en sistema")
        plt.show()


        input("Pulsa una tecla para continuar")
    elif opcionMenu == "4":

        contador_gral = 0
        media_gral = 0
        varianza_gral = 0
        desvio_gral = 0
        media_de_las_medias = []
        varianza_de_las_varianzas = []
        desvio_de__desvios = []
        for i in range(10):
            contador_gral += 1
            MainProgram()
            GraficaPromTiempoSistemaMedia(ListaDemoras)
            plt.title("Media de los tiempos en cola")
            plt.xlabel("Numero de Cliente")  # título del eje x
            plt.ylabel("Valor de la media de tiempo en cola")

            GraficaPromTiempoSistemaVarianza(ListaDemoras)
            plt.title("Varianza de los tiempos en cola")
            plt.xlabel("Numero de Cliente")  # título del eje x
            plt.ylabel("Valor de la varianza de tiempo en cola")

            GraficaPromTiempoSistemaDesvio(ListaDemoras)
            plt.title("Desviacion de los tiempos en cola")
            plt.xlabel("Numero de Cliente")  # título del eje x
            plt.ylabel("Valor de la desviacion de tiempo en cola")
        plt.show()


        input("Pulsa una tecla para continuar")
    elif opcionMenu == "5":
        contador_gral = 0
        media_gral = 0
        varianza_gral = 0
        desvio_gral = 0
        media_total_utlizacion_servidor=0
        media_de_las_medias = []
        varianza_de_las_varianzas = []
        desvio_de__desvios = []
        for i in range(10):
            contador_gral += 1
            MainProgram()
            GraficaPromClientesSistemaMedia(utilizacion_servidor_total)
            plt.title("Media de utilización del servidor")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Valor de la media de utilización del servidor")

            GraficaPromClientesSistemaVarianza(utilizacion_servidor_total)
            plt.title("Varianza de utilización del servidor")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Valor de la varianza de utilización del servidor")

            GraficaPromClientesSistemaDesvio(utilizacion_servidor_total)
            plt.title("Desviacion de utilización del servidor")
            plt.xlabel("Tiempo(segundos)")  # título del eje x
            plt.ylabel("Valor de la desviación utilización del servidor")
        
        plt.figure(4)
        PastelUtilizacionServidor()
        plt.title("Porcentaje total del tiempo que el servidor se encuentra ocupado ")
        plt.show()

        input("Pulsa una tecla para continuar")

    elif opcionMenu == "6":
        numero_clientes_cola = input("Ingresar numero de clientes en cola : ")

        prob_n_clientes_cola = ((1-(1/mean_interarrival)/(1/mean_service)) *((1/mean_interarrival)/(1/mean_service))**int(numero_clientes_cola))
        print("La probabilidad de que haya: " + str(numero_clientes_cola) +" clientes en cola es de:"+str(prob_n_clientes_cola))
        
        PastelProbabilidadClienteCola()

        plt.show()
        input("Pulsa una tecla para continuar")
    elif opcionMenu == "0":
        break
    else:
        print(" ")
        input("No has pulsado ninguna opción correcta... \n Pulsa una tecla para continuar")






