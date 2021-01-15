# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:28:03 2020

@author: Admin
"""

def tieneRestriccion(patente, catalitico, dia):
    if '-' in patente:
        letraRestriccion = patente[1]
    elif ' ' in patente:
        letraRestriccion = patente[3]
        
    if dia.upper() == 'LUNES':
        if catalitico:
            if ord(letraRestriccion) >= ord('A')\
            and ord(letraRestriccion) <= ord('G'):
                return True
            else:
                return False
        else:
            if int(patente[-1]) in [0,1,2,3]:
                return True
            else:
                return False
        
    elif dia.upper() == 'MIERCOLES':
        if catalitico:
            if ord(letraRestriccion) > ord('G')\
            and ord(letraRestriccion) <= ord('N'):
                return True
            else:
                return False
        else:
            if int(patente[-1]) in [4,5,6]:
                return True
            else:
                return False
        
    elif dia.upper() == 'VIERNES':
        if catalitico:
            if ord(letraRestriccion) > ord('N')\
            and ord(letraRestriccion) <= ord('Z'):
                return True
            else:
                return False
        else:
            if int(patente[-1]) in [7,8,9]:
                return True
            else:
                return False
        
    else:
        return False