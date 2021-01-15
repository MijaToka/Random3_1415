from conjuntoList import union,inter,resta,leer,grabarConjunto

#monoCurso conjunto que estan en solo 1 curso
def enUno(A,B,C):
    soloA = resta(A,union(B,C))
    soloB = resta(B,union(A,C))
    soloC = resta(C,union(B,A))
    return union(soloA,union(soloB,soloC))

#biCurso conjunto que estan en solo 2 cursos
def enDos(A,B,C):
    AB = resta(inter(A,B),C)
    AC = resta(inter(A,C),B)
    BC = resta(inter(C,B),A)
    return union(AB,union(AC,BC))

#triCurso
def enTres(A,B,C):
    return inter(A,inter(B,C))

#anyCurso
def enAny(A,B,C):
    return union(A,union(B,C))

#PROGRAMA  
#Directorios
dirA = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/Tarea Cursos/txt conjuntos/cursoA.txt'
dirB = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/Tarea Cursos/txt conjuntos/cursoB.txt'
dirC = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/Tarea Cursos/txt conjuntos/cursoC.txt'
dir1 = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/Tarea Cursos/txt conjuntos/1curso.txt'
dir2 = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/Tarea Cursos/txt conjuntos/2curso.txt'
dir3 = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/Tarea Cursos/txt conjuntos/3curso.txt' 
dirAny = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/Tarea Cursos/txt conjuntos/anyCurso.txt' 

#Conjuntos
A = leer(dirA)
B = leer(dirB)
C = leer(dirC)

EnUno = enUno(A,B,C)
EnDos = enDos(A,B,C)
EnTres = enTres(A,B,C)
EnAny = enAny(A,B,C)

#Archivos
grabarConjunto(EnUno,dir1)
grabarConjunto(EnDos,dir2)
grabarConjunto(EnTres,dir3)
grabarConjunto(EnAny,dirAny)

