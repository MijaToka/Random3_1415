"""Modulo 'listaVisual.py', por jeremy@barbay.cl [2020-11-12 Thu]

Extension (y correccion  parcial) del modulo 'lista.py', autor desconocido.

Permite generar una representacion graphica de la lista creada via la funcion 'dibuja(lista)'.
"""
import estructura

import graphviz
from IPython.display import display_svg, SVG, display



# Diseno de la estructura
# lista : valor (any = cualquier tipo) siguiente (lista)
estructura.crear("lista", "valor siguiente")

# identificador para listas vacias
listaVacia = None

# crearLista: any lista -> lista
# devuelve una lista cuya cabeza es valor
# y la cola es resto
def crearLista(valor, resto):
        return lista(valor, resto)

# cabeza: lista -> any
# devuelve la cabeza de una lista (un valor)
def cabeza(lista): 
	return lista.valor

# cola: lista -> lista
# devuelve la cola de una lista (una lista)
def cola(lista):
	return lista.siguiente

# vacia: lista -> bool
# devuelve True si la lista esta vacia
def vacia(lista):
	return lista == listaVacia


def dibuja(lista, dibujaPunteroVacillo = False, dibujaPunteroInicial = False):
  """Dibuja una lista en svg.
  Si @dibujaPunteroInicial esta True, dibuja un nodo con el puntero inicial.
  Si @dibujaPunteroVacillo esta True, dibuja un nodo "lista vacilla" al final de la lista.

  Jérémy 'Le JyBy' Barbay, jeremy@barbay.cl
  """
  display = graphviz.Digraph()
  display.format = 'svg'
  if vacia(lista):
    display.node("Lista Vacia")
  else:
    display.node(repr(lista),cabeza(lista))
    if dibujaPunteroInicial:
      display.node("puntero inicial")
      display.edge("puntero inicial",repr(lista))
    while not vacia(cola(lista)):
       display.node(repr(cola(lista)),cabeza(cola(lista)))
       display.edge(repr(lista),repr(cola(lista)))
       lista = cola(lista)
    if dibujaPunteroVacillo:
      display.node("lista vacia")
      display.edge(repr(lista),"lista vacia")
  svg = display.pipe().decode('utf-8')
  return SVG(svg)



# Tests

test_lista = crearLista(1, crearLista(2, crearLista(3, listaVacia)))

assert cabeza(test_lista) == 1
assert cabeza(cola(test_lista)) == 2
assert cabeza(cola(cola(test_lista))) == 3
assert cola(cola(test_lista)) == crearLista(3, listaVacia)

assert vacia(listaVacia)
assert not vacia(test_lista)
assert vacia(cola(cola(cola(test_lista))))

