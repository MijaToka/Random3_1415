import math
import estructura
import lista

def mapa(operacion,unaLista):
    if lista.vacia(lista):
        return None
    return lista.unaLista(operacion(lista.cabeza(unaLista)) , mapa(operacion,lista.cola(unaLista)))

def fold(operacion,init,unaLista):
    if lista.vacia(lista.cola(unaLista)):
        return operacion(init,lista.cabeza(unaLista))
    return fold(operacion,operacion(init,lista.cabeza(unaLista)),lista.cola(unaLista))

def filtro(operacion,condicion,unaLista):
    if lista.vacia(unaLista):
        return None
    elif operacion(lista.cabeza(unaLista),condicion):
        return lista.crearLista(lista.cabeza(unaLista),\
                filtro(operacion,condicion,lista.cola(unaLista)))
    else:
        return filtro(operacion,condicion,lista.cola(unaLista))
    
estructura.crear('fraccion','nom den')

def simplifica(Fraccion):
    Num = Fraccion.num // math.gcd(Fraccion.num,Fraccion.den)
    Den = Fraccion.den // math.gcd(Fraccion.num,Fraccion.den)
    return fraccion(Num,Den)
    
def invertir(Fraccion):
    assert not Fraccion.num == 0, "You can't divide by 0"       
    return fraccion(Fraccion.den,Fraccion.num)

def sumaFrac(fraccion1,fraccion2):
    Num = fraccion1.num * fraccion2.den + fraccion1.den * fraccion2.num
    Den = fraccion1.den * fraccion2.den
    return simplifica(fraccion(Num,Den))

def esMenor(fraccion1,fraccion2):
    return fraccion1.num/fraccion1.den < fraccion2.num/fraccion2.den

def mapInvertir(listaFrac):
    return mapa(invertir,listaFrac)

def foldSuma(listaFrac):
    return fold(sumaFrac,0,listaFrac)

def filtroMenor(listaFrac,fraccionRef):
    return filtro(esMenor,fraccionRef,listaFrac)