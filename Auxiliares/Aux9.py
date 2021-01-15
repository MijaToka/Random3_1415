curso = []
notas = []

def insertarNota(nombre,nota,curso,notas):
    curso.append(nombre); notas.append(nota)
    return

def quitarNota(nombre,curso,notas):
    for i in range(len(curso)):
        if curso[i] == nombre:
            curso.remove(nombre)
            return notas.pop(i)
    return 'El alumno no cursa el ramo'

def consultarNota(nombre,curso,notas):
    for i in range(len(curso)):
        if curso[i] == nombre:
            return notas[i]

def mostrarNotas(curso,notas):
    for i in range(len(curso)):
        print(f'Alumno: {curso[i]} Nota: {notas[i]}')
    return

def promedio(notas): 
    return sum(notas) / len(notas)


def start(curso = [], notas = []):
    opcion = input('Eliga qué opción quiere ejecutar (Ingrese el número de selección)\n1. Agregar nota\n2. Quitar nota\n3. Consultar nota\n4. Mostar notas\n5. Promedio\n6. Nada (Se acaba el programa)\n')
    if opcion == '1':
        print(insertarNota(input('Nombre: '), float(input('Nota: ')), curso, notas))
    elif opcion == '2':
        print(quitarNota(input('Nombre: '), curso, notas))
    elif opcion == '3':
        print(consultarNota(input('Nombre: '), curso, notas))
    elif opcion == '4':
        print(mostrarNotas(curso,notas))
    elif opcion == '5':
        print(promedio(notas))
    elif opcion == '6':
        return False
    print('')
    return True



def esPalindromo(string):
    for i in range(len(string)):
        if not string[i] == string[-i-1]:
            return False
    return True

##PROGRAMA
true = False
#true = True
while true:
    true = start()

