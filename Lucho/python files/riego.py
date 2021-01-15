import random

def riego(hectáreas,tipo_de_suelo, humedad_de_suelo, probabilidad_de_lluvia):

    if (hectáreas <= 0):
        print("Las hectáreas no pueden ser menores o iguales a 0.")
    elif(humedad_de_suelo > 700) and (humedad_de_suelo <= 1000) :
        print( "No hay necesidad de regar debido a que la humedad de suelo es ", humedad_de_suelo, ".")
    elif (humedad_de_suelo > 1024):
        print("La lectura de la humedad de suelo no puede ser mayor a 1024, por favor inténtelo de nuevo.")
    elif (probabilidad_de_lluvia > 70) and (probabilidad_de_lluvia <=100) :
        print("No hay que regar debido a que la probabilidad de lluvia es ", probabilidad_de_lluvia, "%")
    elif (probabilidad_de_lluvia > 100):
        print("La lectura de probabilidad de lluvia no puede ser mayor a 100, por favor inténtelo de nuevo.")
    elif (tipo_de_suelo == "Suelo inválido"):
        print("La lectura de suelo es inválida, por favor inténtelo de nuevo.")
    else:
      if (tipo_de_suelo == "Arcilloso"):
          caudal = 1
          tiempo_x_ciclo = 2
          número_de_ciclos = 2
      elif (tipo_de_suelo == "Arenoso"):
          caudal = 2
          tiempo_x_ciclo = 2
          número_de_ciclos = 5
      elif (tipo_de_suelo == "Limoso"):
          caudal = 3
          tiempo_x_ciclo = 5
          número_de_ciclos = 2
          

      if (tipo_de_suelo != "Suelo Inválido") and (humedad_de_suelo <= 700) \
         and (probabilidad_de_lluvia <= 70) and (hectáreas > 0):
           cantidad_de_agua = caudal*tiempo_x_ciclo*número_de_ciclos*hectáreas
           print("Usted tiene un suelo", tipo_de_suelo,", por lo tanto usted deberá regar",\
                 número_de_ciclos, "veces al día, durante", tiempo_x_ciclo,\
                 "minutos, con un caudal de", caudal, "litro(s) por minuto.")
           print("En total usted gastará", cantidad_de_agua,"litros al día.")
           


h = int(input("Ingrese número de hectáreas "))
hum = int(random.randint(0,1024))
lluvia = int(random.randint(0,100))
suelo = str(random.choice(["Arcilloso","Limoso","Arenoso","Suelo inválido"]))
riego(h,suelo,hum,lluvia)