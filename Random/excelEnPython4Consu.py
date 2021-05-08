import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

DIR = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Random/'

datos = pd.read_excel(DIR+'Ejercicio_2_1.xlsx')

Equipos = datos['EQUIPO']
Publico = datos['PUBLICO']

dick = {}
for i in range(len(Equipos)):

    if not Equipos[i] in dick:
        dick[Equipos[i]] = [0]

    dick[Equipos[i]][0] += Publico[i]
    dick[Equipos[i]].append(Publico[i])



iWillHaveOrder = []

for equipo in dick:
    iWillHaveOrder.append((equipo, dick[equipo][0]))
    
iWillHaveOrder.sort(key=lambda x:x[1],reverse=True)

MayorVentas, MenorVentas = [],[]
for i in range(3):
    MayorVentas.append(iWillHaveOrder[i])
    MenorVentas.append(iWillHaveOrder[len(iWillHaveOrder)-1-i])

print("Los 3 equipos que más vendieron fueron.")

for i in range(3):
    print(f'{i+1}. {MayorVentas[i][0]}: {MayorVentas[i][1]}')
print()
print("Los 3 equipos que menos vendieron fueron.")

for i in range(3):
    print(f'{i+1}.- {MenorVentas[i][0]}: {MenorVentas[i][1]}')

print()
print("El máximo vendido en un partido de:")
lst=['U LA CALERA','HUACHIPATO']
for equipo in lst:
    print(f"{equipo}: {max(dick[equipo][1:])}")
print()
#print(dick)