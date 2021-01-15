##FUNCIONES NO USADAS
def datosClase(archivo):
    """Recibe una direccion de un archivo el cual tiene infomacion 
    (en formato nombre;tipoVihiculo;patente;horaIngreso;horaSalida\n ...) 
    y entrega una matriz cuyas filas son una lista con los datos del tipo de la fila.

    datosPersona: str -> list(list)
    
    e.g.: datosPersona(registro.txt)
        registro.txt -> Mijail;Automovil;SA1460;10:30;11:20\n
                        Pablo;Moto;JKL420;12:12;15:00\n
                        Luis;Automovil;CPYT45;13:30;14:10\n
        ->  [['Mijail', 'Pablo', 'Luis'],
             ['Automovil','Moto','Automovil'],
             ['SA1460','JKL420','CPYT45'],
             ['10:30','12:12','13:30'],
             ['11:20','15:00','14:10']]
    
    """
    matrix = [[],[],[],[],[]]
    #matrix = [nombre,tipo,patente,horaIn,horaOut]
    file = open(archivo,'r')

    for line in file:
        datos = line.strip().split(';')
        for i,dato in enumerate(datos):
            matrix[i].append(dato)
    
    file.close()
    return matrix      

def tipoVehiculos_Clase(datos_Clase):
    """Recibe una matriz del formato entregado por la funcion datosClase 
    y entrega una lista de los tipos de vahiculos que hay en la matriz.

    tipoVehiculos: list(list) -> list

    e.g.: datos_Clase = [['Mijail', 'Pablo', 'Luis'],
                        ['Automovil','Moto','Automovil'],
                        ['SA1460','JKL420','CPYT45'],
                        ['10:30','12:12','13:30'],
                        ['11:20','15:00','14:10']]

            tipoVehiculos(datos_Clase) -> ['Automovil','Moto']             
    """
    tiposV = []

    for tipo in datos_Clase[1]:
        if tipo not in tiposV:
            tiposV.append(tipo)
        
    return tiposV 
#FUNCIONES
def tiempoEstacionado(entrada,salida):
    '''Recibe 2 strings con horas (con formato HH:MM) de entrada y salida 
        y calcula el tiempo en minutos entre ambas.
        tiempoEstacionado: str str -> int
        e.g.: tiempoEstacionado("10:20","11:10") -> 50
    '''
    assert type(entrada) == str and type(salida) == str, \
        'Input must be str'
    strhIn,strmIn = entrada.split(':')
    strhOut,strmOut = salida.split(':')
    
    horaIn,horaOut = int(strhIn),int(strhOut)
    minIn,minOut = int(strmIn),int(strmOut)
    
    difHora = horaOut - horaIn
    difMin = minOut - minIn
    
    if difMin < 0:
        difMin += 60
        difHora -= 1
    
    return difHora * 60 + difMin

def datosPersona(archivo):
    """Recibe una direccion de un archivo el cual tiene infomacion 
        (en formato nombre;tipoVihiculo;patente;horaIngreso;horaSalida\n ...) 
        y entrega una matriz cuyas filas son una lista con los datos de la persona.

        datosPersona: str -> list(list)
    
        e.g.: datosPersona(registro.txt)
            registro.txt -> Mijail;Automovil;SA1460;10:30;11:20\n
                            Pablo;Moto;JKL420;12:12;15:00\n
                            Luis;Automovil;CPYT45;13:30;14:10\n
            ->  [['Mijail', 'Automovil', 'SA1460', '10:30', '11:20'],
                ['Pablo', 'Moto', 'JKL420', '12:12', '15:00'],
                ['Luis', 'Automovil', 'CPYT45', '13:30', '14:10']]
    """
    datoslst = []
    file = open(archivo,'r')

    for line in file:
        datos = line.strip().split(';')
        datoslst.append(datos)

    file.close()
    return datoslst

def tipoVehiculos_Persona(datos_Persona):
    """Recibe una matriz del formato entregado por la funcion datosClase 
        y entrega una lista de los tipos de vahiculos que hay en la matriz.
    
        tipoVehiculos: list(list) -> list
    
        e.g.: datos_Persona =   [['Mijail', 'Automovil', 'SA1460', '10:30', '11:20'],
                                ['Pablo', 'Moto', 'JKL420', '12:12', '15:00'],
                                ['Luis', 'Automovil', 'CPYT45', '13:30', '14:10']]
            
                tipoVehiculos_Persona(datos_Persona) -> ['Automovil','Moto']
    """
    tiposV = []

    for persona in datos_Persona:
        if persona[1] not in tiposV:
            tiposV.append(persona[1])

    return tiposV 

def totalVehiculos(datos_Persona):
    """Recibe una matriz del formato entregado por la funcion datosPersona 
        y entrega la cantidad de personas que tiene esta matriz.

        totalVehiculos: list(list) -> int

        e.g.: datos_Persona =   [['Mijail', 'Automovil', 'SA1460', '10:30', '11:20'],
                                ['Pablo', 'Moto', 'JKL420', '12:12', '15:00'],
                                ['Luis', 'Automovil', 'CPYT45', '13:30', '14:10']]
            
                totalVehiculos(datos_Persona) -> 3
    """
    return len(datos_Persona)

def dictTipos(datos_Persona):
    """Recibe una matriz del formato entregado por la funcion datosPersona 
        y entrega un diccionario cuyas llaves son los tipos de vehiculo de una persona 
        y los valores son una matriz cuyas filas son una lista ordenada segun el tiempo
        estacionado (de mayor a menor) con los datos de la persona cuyo vehiculo es del tipo de la llave.

        dictTipos: list(list) -> dict

        e.g.: datos_Persona =   [['Mijail', 'Automovil', 'SA1460', '10:30', '11:20'],
                                ['Pablo', 'Moto', 'JKL420', '12:12', '15:00'],
                                ['Luis', 'Automovil', 'CPYT45', '13:30', '14:10']]

                dictTipos(datos_Persona) -> {'Automovil':   [['Mijail', 'Automovil', 'SA1460', '10:30', '11:20'],
                                                            ['Luis', 'Automovil', 'CPYT45', '13:30', '14:10']],
                                            'Moto': ['Pablo', 'Moto', 'JKL420', '12:12', '15:00']}              
    """
    dicc = {}
    tiposlst = tipoVehiculos_Persona(datos_Persona)
    
    for tipo in tiposlst:
        dicc[tipo] = []

    for persona in datos_Persona:
        dicc[persona[1]].append(persona)

    for tipo in dicc:
        dicc[tipo].sort(key= lambda persona: tiempoEstacionado(persona[-1],persona[-2]))

    return dicc

def vehiculosMaxTiempo(datos_Persona):
    """Recibe una matriz del formato entregado por la funcion datosPersona 
        y entrega una lista de los datos de la persona que más tiempo lleva estacionada
        por tipo de vehiculo.

        vehiculosMaxTiempo: list(list) -> list

        e.g.: datos_Persona =   [['Mijail', 'Automovil', 'SA1460', '10:30', '11:20'],
                                ['Pablo', 'Moto', 'JKL420', '12:12', '15:00'],
                                ['Luis', 'Automovil', 'CPYT45', '13:30', '14:10']]

                vehiculosMaxTiempo(datos_Persona) ->    [['Mijail', 'Automovil', 'SA1460', '10:30', '11:20'],
                                                        ['Pablo', 'Moto', 'JKL420', '12:12', '15:00']]
    """
    dicc = dictTipos(datos_Persona)
    lstMax = []

    for tipo in dicc:
        lstMax.append(dicc[tipo][0])
    
    return lstMax
        

#VARIABLES

DIRECTORIO_ACTUAL = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Lucho/.txt registros/'
REGISTRO = DIRECTORIO_ACTUAL + 'registros.txt'

#PROGRAMA

datos_Persona = datosPersona(REGISTRO)
dicc = dictTipos(datos_Persona)

for tipo in dicc:
    file = open(DIRECTORIO_ACTUAL + tipo + '.txt','w')
    
    for i,persona in enumerate(dicc[tipo]):
        file.write(f'{i+1} - El vehiculo de {persona[0]} con patente {persona[2]} estuvo estacionado {tiempoEstacionado(persona[-2],persona[-1])} minutos.\n')
    
    file.close()


maxTiempo = vehiculosMaxTiempo(datos_Persona)
print('Vehículos con mayor tiempo de estacionamiento, por tipo:')
for persona in maxTiempo:
    print(f'    {persona[1]}: {persona[2]} ({persona[0]})')
print(f'Total de vehiculos en el día: {totalVehiculos(datos_Persona)}')