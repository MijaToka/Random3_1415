
DIRECTORIO = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Lucho/.txt Locales/'
ARCHIVO = DIRECTORIO + 'locales.txt'

from math import sqrt
def distancia(x,y):
    return sqrt((x**2)+(y**2))

def filtrar_locales(nombre_archivo, rango):
    file=open(nombre_archivo, "r")
    lista_rango=[]
    i=0
    for line in file:
        datos=line.strip().split(";")
        x,y=datos[2].split(",")
        lista_rango.append(datos)
        
        if distancia(int(x),int(y))<=rango:
            i+=1

    dicc={}
    for restaurant in lista_rango:
        if not restaurant[1] in dicc:
            dicc[restaurant[1]]=[]
        
        x,y=restaurant[2].split(",")
        if distancia(int(x),int(y))<=rango:
            dicc[restaurant[1]].append(restaurant)
    
    for tipo in dicc:
        file_tipo=open(DIRECTORIO+tipo+".txt","w")
        
        if dicc[tipo] != []:
            file_tipo.write(f"Locales de tipo {tipo} que están a distancia {rango} o menos:\n")
        
        dicc[tipo].sort(key=lambda restaurant: restaurant[4])
        
        for restaurant in dicc[tipo]:
            file_tipo.write(f"\t{restaurant[0]}, calificación {restaurant[3]}, precio: {restaurant[4]}.\n")
        file_tipo.close()
    
    file.close()
    
    return i

print(filtrar_locales(ARCHIVO,10))