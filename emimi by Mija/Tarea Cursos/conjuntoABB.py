#%%IMPORTS
from ABB import insertar

#%%FUNCIONES
def inOrder(abb):
  if abb == None: return []
  else:
    return inOrder(abb.izq) + [abb.valor] +  inOrder(abb.der)

def pertenece(x,ABB):
    if ABB == None: return False
    if x == ABB.valor: return True
    if x < ABB.valor: return pertenece(x,ABB.izq)
    if x > ABB.valor: return pertenece(x,ABB.der)

def hayRepetidos(A):
    if A == None: return False
    if pertenece(A.valor,A.izq) or pertenece(A.valor,A.der):
        return True
    return hayRepetidos(A.izq) or hayRepetidos(A.der) 

def esConjunto(A):
    return not hayRepetidos(A)

def union(ABB1,ABB2):
    for item in inOrder(ABB1):
        ABB2 = insertar(item,ABB2)
    return ABB2

def inter(ABB1,ABB2):
    ABBexit = None
    for item in inOrder(ABB1):
        if pertenece(item,ABB2):
           ABBexit = insertar(item,ABBexit) 
    return ABBexit
            
def resta(ABB1,ABB2):
    ABBexit = None
    for item in inOrder(ABB1):
        if not pertenece(item,ABB2):
            ABBexit = insertar(item,ABBexit)
    return ABBexit

def leer(pregunta='elemento?',fin='.',A=None):
    valor=input(pregunta)
    if valor==fin: 
        return A
    else:
        return leer(pregunta,fin,insertar(valor,A))
    
def escribir(ABB):
    if ABB == None: return
    escribir(ABB.izq)
    print(ABB.valor)
    escribir(ABB.der)
    
#%%