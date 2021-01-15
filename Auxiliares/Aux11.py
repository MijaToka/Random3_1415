#FILE NAMES
DIRECTORIO = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Auxiliares/txt Aux/'
NOTAS = DIRECTORIO + 'notas.txt'
MASCOTAS = DIRECTORIO + 'mascotas.txt'

#FUNCIONES (NOTAS)

def datosNotas(directory):
    file = open(directory,'r')
    nombre_notas = []
    
    for line in file:
        persona = line.strip().split(',')
        nombre = persona[0]; notas = persona[1:]
        nombre_notas.append((nombre,notas))
    
    file.close()
    return nombre_notas

#print(datosNotas(NOTAS))

def promedio(notasLts):
    return sum(list(map(float,notasLts))) / len(notasLts)

def promedioNotas(directory):
    datos = datosNotas(directory)
    file = open(DIRECTORIO + 'promedios.txt','w')
    
    for persona in datos:
        file.write(f'{persona[0]},{promedio(persona[1])}\n')
    
    file.close()
    return
#promedioNotas(NOTAS)

#FUNCIONES (MASCOTAS)

def datosMascotas(directory):
    mascotas = []
    file = open(directory, 'r')
    
    for i,line in enumerate(file):
        mascotas.append((line.strip(),i+1))
    
    file.close()
    return mascotas

def ordenar(directory):
    mascotas = datosMascotas(directory)
    mascotas.sort(key=lambda mascota: mascota[0])
    
    for mascota in mascotas:
        print(f'{mascota[0]} {mascota[1]}')
    
    return mascotas

#ordenar(MASCOTAS)