# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:10:04 2020

@author: Admin
"""

from ABB import insertar

def pertenece(x,A):
  if A == None:
    return False
  if x == A.valor:
    return True
  if x < A.valor:
    return pertenece(x, A.izq)
  if x > A.valor:
    return pertenece(x, A.der)

def esConjunto(A):
  if A == None:
    return True
  if pertenece(A.valor,A.izq) or pertenece(A.valor, A.der):
    return False
  else:
    return esConjunto(A.izq) and esConjunto(A.der)

def union(x,y):
  assert esConjunto(x) and esConjunto(y)
  if x == None:
    return y 
  y = union(x.izq,y)
  y = insertar(x.valor,y)
  y = union(x.der,y)
  return y

def inter(x, y, fin=None):
    if x == None:
        return fin
    fin = inter(x.izq,y,fin)
    if pertenece(x.valor,y):
        fin =  insertar(x.valor,fin)
    fin = inter(x.der, y, fin)
    return fin

def resta(x, y, fin=None):
  if x == None:
    return fin
  fin = resta(x.izq, y, fin)
  if not pertenece(x.valor, y):
    fin= insertar(x.valor, fin)
  fin = resta(x.der, y, fin)
  return fin

def sonIguales(x, y):
  return union(resta(x,y),resta(y,x)) == None

def leer(pregunta= 'elemento?', fin='.', A=None):
  valor= input(pregunta)
  if valor==fin:
    return A
  return leer(pregunta, fin, insertar(valor,A))

def escribir(x):
  if x == None:
    return
  escribir(x.izq)
  print(x.valor)
  escribir(x.der)
