# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:18:52 2020

@author: emi
"""


import jugadaemi as j
import random as r
def cachipun(n):
    p=j.jugada(n)
    c=j.jugada(r.randint(1,3))
    if p==c:
        game="empate"
    elif (p==j.jugada(1) and c==j.jugada(3)) or (p==j.jugada(2) and c==j.jugada(1)) or (p==j.jugada(3) and c==j.jugada(2)):
        game="gana jugador"
    
    elif (p==j.jugada(3) and c==j.jugada(1)) or (p==j.jugada(1) and c==j.jugada(2)) or (p==j.jugada(2) and c==j.jugada(3)):
        game="gana computador"
    print("Ud. jugó "+str(p))
    print("Computador jugó "+str(c))
    print(str(game))