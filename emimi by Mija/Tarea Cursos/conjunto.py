from lista import crearLista,cola,cabeza,fold,mapa

def hayRepetidos(unaLista):
    if unaLista == None: return False
    if cola(unaLista) == None : return False
    boollista = mapa(lambda x:x==cabeza(unaLista),cola(unaLista))
    return fold(lambda init,x:init or x, False,boollista) \
        or hayRepetidos(cola(unaLista))
        
def esConjunto(unaLista):
    return not hayRepetidos(unaLista)

def volverConjunto(unaLista,exitlist=None):
    if cola(unaLista) == None:
        return crearLista(cabeza(unaLista),exitlist)
    else:
        boollista = mapa(lambda x:x==cabeza(unaLista),cola(unaLista))
        if not fold(lambda init,x:init or x, False,boollista):
            return volverConjunto(cola(unaLista),\
                                  crearLista(cabeza(unaLista),exitlist))
        else:
            return volverConjunto(cola(unaLista),exitlist)                    

def union(lista1,lista2):
    if not esConjunto(lista1):
        lista1 = volverConjunto(lista1)
    if not esConjunto(lista2):
        lista2 = volverConjunto(lista2)
    if lista1 == None:
        return lista2
    addList = crearLista(cabeza(lista1),lista2)
    if hayRepetidos(addList):
        return union(cola(lista1),lista2)
    else:
        return union(cola(lista1),crearLista(cabeza(lista1),lista2))
    
def inter(lista1,lista2,exitlist = None):
    if not esConjunto(lista1):
        lista1 = volverConjunto(lista1)
    if not esConjunto(lista2):
        lista2 = volverConjunto(lista2)
    if lista1 == None:
        return exitlist
    addList = crearLista(cabeza(lista1),lista2)
    if hayRepetidos(addList):
        return inter(cola(lista1),lista2,crearLista(cabeza(lista1),exitlist))
    else:
        return inter(cola(lista1),lista2,exitlist)

def resta(lista1,lista2,exitlist = None):
    if not esConjunto(lista1):
        lista1 = volverConjunto(lista1)
    if not esConjunto(lista2):
        lista2 = volverConjunto(lista2)
    if lista1 == None:
        return exitlist
    addList = crearLista(cabeza(lista1),lista2)
    if hayRepetidos(addList):
        return resta(cola(lista1),lista2,exitlist)
    else:
        return resta(cola(lista1),lista2,crearLista(cabeza(lista1),exitlist))
        
def pertenece(x,unaLista):
    if unaLista == None:
        return False
    if x == cabeza(unaLista):
        return True
    else:
        return pertenece(x,cola(unaLista))
    
def leer(pregunta='elemento?',fin='.'):
    cola = None
    while True:
        elemento = input(pregunta+' ')
        if elemento == fin:
            break
        cola = crearLista(elemento,cola)
    return cola 
   
def escribir(unaLista):
    if unaLista == None: return None
    if cola(unaLista) == None: 
        print(cabeza(unaLista))
    else:
        print(cabeza(unaLista))
        escribir(cola(unaLista))