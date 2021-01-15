#VARIABLES

DIRECTORIO_ACTUAL = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Lucho/.txt Juegos/'
ARCHIVO = DIRECTORIO_ACTUAL + 'juegos.txt'

#FUNCIONES

def datos(nombreArchivo):
    datosLst = []
    file = open(nombreArchivo,'r')

    for line in file:
        datosJuego = line.strip().split(';')
        datosLst.append(datosJuego)

    file.close()
    
    return datosLst

def generos(datosJuegos):
    generosLst = []

    for juego in datosJuegos:
        _,_,generosStr,_,_,_,_,_,_ = juego
        generos = generosStr.split(',')
        for genero in generos:
            if genero not in generosLst:
                generosLst.append(genero)
    
    return generosLst

def dictGeneros(datosJuegos):
    dicc = {}
    generosLst = generos(datosJuegos)

    for genero in generosLst:
        dicc[genero] = []

    for juego in datosJuegos:
        generosJuego = juego[2].split(',')
        for genero in generosJuego:
            dicc[genero].append(juego)

    return dicc 

def first3Sort(matrix,keyIndex = 0):
    index1st = 0; index2nd = 0; index3rd = 0
    
    for i,lst in enumerate(matrix):
        #En particular lst = datosJuego y matrix lista de juegos (separados por genero)
        
        if lst[keyIndex] >= matrix[index1st][keyIndex]:
            index3rd = index2nd
            index2nd = index1st
            index1st = i
        
        elif lst[keyIndex] >= matrix[index2nd][keyIndex]:
            index3rd = index2nd
            index2nd = i
        
        elif lst[keyIndex] >= matrix[index3rd][keyIndex]:
            index3rd = i

    return index1st,index2nd,index3rd

def rankear(datosJuegos):
    generosLst = generos(datosJuegos)
    dicc = dictGeneros(datosJuegos)
    contador = 0

    for genero in generosLst:
        file = open(DIRECTORIO_ACTUAL + genero + '.txt','w')
        file.write(genero + '\n')
        contador += 1
        
        indexes = first3Sort(dicc[genero],4)
        
        for index in indexes:
            juego = dicc[genero][index]
            file.write(f'   {juego[0]} ({juego[-3]})\n')

        file.close()

    return contador

#PROGRAMA   

datosJuegos = datos(ARCHIVO)