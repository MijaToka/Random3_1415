# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:19:21 2020

@author: Admin
"""


def oladyi(cantidad):
    kefir = cantidad * 100
    bicarbonato = cantidad / 4 
    azucar = int(cantidad  / 3 * 100) / 100
    azucar2 = cantidad / 2
    sal = int(cantidad / 3 * 5 * 100) / 100
    harina = cantidad / 2
    
    print('Necesitas:')
    print('-' + str(kefir) +' ml de kefir.')
    print('-' + str(bicarbonato) + ' cucharaditas de bicarbonato.')
    print('-' + str(azucar) + ' ~ ' + str(azucar2) + ' cucharadas de azucar.')
    print('-' + str(sal) +'g de sal.')
    print('-' + str(harina) + ' vazo(s) (' + str(200 * harina) +' ml) de harina')
    

n= int(input('¿Cuantas porciones de oladyi quieres hacer? '))
oladyi(n)