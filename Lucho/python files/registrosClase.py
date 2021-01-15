#VARIABLES

DIRECTORIO_ACTUAL = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Lucho/.txt registros/'
REGISTRO = DIRECTORIO_ACTUAL + 'registros.txt'

#FUNCIONES Y CLASE
class Persona:
    def __init__(self,lstDatos):
        self.nombre = lstDatos[0]
        self.tipo = lstDatos[1]
        self.patente = lstDatos[2]
        self.horaEntrada = lstDatos[3]
        self.horaSalida = lstDatos[4]
        self.tiempoEstacionado = 0
        self.tiempoRegistrado()
    
    def __str__(self):
        return f'Nombre: {self.nombre}\nTipo: {self.tipo}\nPatente: {self.patente}\nHora Ingreso: {self.horaEntrada}\nHora Salida: {self.horaSalida}\nTiempo Estacionado: {self.tiempoEstacionado}'

    def tiempoRegistrado(self):
        strhIn,strmIn = self.horaEntrada.split(':')
        strhOut,strmOut = self.horaSalida.split(':')

        hIn,hOut = int(strhIn),int(strhOut)
        minIn,minOut = int(strmIn),int(strmOut)

        self.tiempoEstacionado += (hOut * 60 + minOut) - (hIn*60 + minIn)
 
def lstDatosAlstPersona(datos):
    personaLst = []

    for dato in datos:
        personaLst.append(Persona(dato))
    
    return personaLst

def datos(archivo):
    datoslst = []
    file = open(archivo,'r')

    for line in file:
        dato = line.strip().split(';')
        datoslst.append(dato)

    file.close()

    return lstDatosAlstPersona(datoslst)

def tipoVehiculos(dato_Persona):
    tipos = []

    for persona in dato_Persona:
        if persona.tipo not in tipos:
            tipos.append(persona.tipo)

    return tipos

def totalVehiculos(dato_Persona):
    lstTipos = tipoVehiculos(dato_Persona)
    return len(lstTipos)

def dictPersonas(datos_Persona):
    lstTipos = tipoVehiculos(datos_Persona)
    dicc = {}

    for tipo in lstTipos:
        dicc[tipo] = []

    for persona in datos_Persona:
        dicc[persona.tipo].append(persona)

    for tipo in dicc:
        dicc[tipo].sort(key= lambda persona: persona.tiempoEstacionado)

    return dicc

def vehiculosMaxTiempo(datos_Persona):
    dicc = dictPersonas(datos_Persona)
    maxTiempo = []
    for tipo in dicc:
        maxTiempo.append(dicc[tipo][-1])
    
    return maxTiempo




#PROGRAMA

datosLst = datos(REGISTRO)
veh = vehiculosMaxTiempo(datosLst)
for dato in veh:
    print(dato)
    print()

print()
