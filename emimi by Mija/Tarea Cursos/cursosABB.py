##%IMPORTS
from conjuntoABB import union,inter,resta,leer,escribir

#%%FUNCIONES

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

#%% MAIN
print('Leyendo curso A')
A = leer()
print('Leyendo curso B')
B = leer()
print('Leyendo curso C')
C = leer()

EnUno = enUno(A, B, C)
EnDos = enDos(A, B, C)
EnTres = enTres(A, B, C)
EnCualquiera = enAny(A, B, C)

print('En un curso')
escribir(EnUno)
print('En dos cursos')
escribir(EnDos)
print('En tres cursos')
escribir(EnTres)
print('En algún curso')
escribir(EnCualquiera)

#%%