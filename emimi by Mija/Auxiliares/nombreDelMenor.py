import fecha
def nombreDelMenor(listaNombre,listaEdad,Hoy):
    nombreMenor = ''
    fechaMenor = 1010001 #Place holder
    for i in range(len(listaNombre)):
        if fecha.esMenor(fechaMenor,listaEdad[i]):
            nombreMenor = listaNombre[i]
            fechaMenor = listaEdad[i]
    edadMenor = fecha.añosTranscurridos(fechaMenor,Hoy)        
    print('edad: ', edadMenor)
    print('nombre del menor: ', nombreMenor)
    print('fecha de nacimiento del menor: ', fechaMenor)

Hoy = int(input('Que dia es hoy(DDMMAAAA) ?'))
listaNombre = []
listaFecha = []
while True:
    Nombre = input('nombre?')
    if Nombre == 'fin':
        break
    listaNombre += [Nombre]
    Fecha = int(input('Fecha de nacimiento(DDMMAAAA) ?'))
    if fecha.esFecha(Fecha):
        listaFecha += [Fecha]
    else:
        listaNombre[:-1]
        print('fecha incorrecta')
        
nombreDelMenor(listaNombre,listaFecha,Hoy)