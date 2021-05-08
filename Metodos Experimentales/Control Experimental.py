import math
#import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

##Datos

T = [0.1, 0.35, 1.32, 2.55, 4.3] #Datos experimentales del Enunciado
P = [0.86 ,0.582 ,0.138, 0.021, 0.002] #\\


xi,yi,xiyi,xi2 = [],[],[],[]
#P = C1 * e**(C2 * T) -(Cambio de variable)-> y = ln(P) = ln(C1) + C2 * T = b + ax
#Por lo tanto yi = ln(Pi), xi = Ti
for i in range(len(T)): #Llena las listas con sus valores correspondientes
    xi.append(T[i])
    yi.append(math.log(P[i],math.exp(1))) #Cambio de variable y = ln(P)
    xiyi.append(xi[i]*yi[i])
    xi2.append(xi[i]*xi[i])


averageY = sum(yi)/len(yi)

##Calculos
#Nota : n = len(xi) = len(yi)
a = (len(xi)*sum(xiyi) - sum(xi)*sum(yi)) / (len(xi)*sum(xi2) - sum(xi)**2)
b = (sum(yi)*sum(xi2) - sum(xiyi)*sum(xi)) / (len(xi)*sum(xi2) - sum(xi)**2)

y_estimado,chi,dPromedio2  = [],[],[]

for i in range(len(xi)): #Datos para calcular Error y R**2
    y_estimado.append(a * xi[i] + b)
    chi.append((a * xi[i] + b - yi[i])**2)
    dPromedio2.append((yi[i]-averageY)**2)

Error = (sum(chi)/(len(chi)-2))**0.5
Correlacion = 1 - sum(chi)/sum(dPromedio2)
    

Calculos = input('Escriba algo en si quiere ver el resultado de los calculos, deje en blanco si solo quiere el gráfico\n')
if Calculos != '':
    print()
    print(f'T: {T}\nP: {P}\n')
    print(f'xi = T: {xi}\n {chr(931)}xi: {sum(xi)}\n')
    print(f'yi = ln(P): {yi}\n {chr(931)}yi: {sum(yi)}\n')
    print(f'xi*yi: {xiyi}\n {chr(931)}xi*yi: {sum(xiyi)}\n')
    print(f'xi^2: {xi2}\n {chr(931)}xi^2: {sum(xi2)}\n')
    print(f'a: {a}  -> C2: {a}\nb: {b}   -> C1: {math.exp(b)}\nError: {Error}\nR**2: {Correlacion}')

#%% Grafico

x, y, yhat = np.array(xi), np.array(yi), np.array(y_estimado)

#plt.style.use(plt.style.available[7])
plt.plot(x,yhat,color='r',markersize=1,label='Regresión lineal')
plt.scatter(x,y,label='Valores medidos')
plt.title('Probabilidad de encontrar un foton (P) vs \n Tiempo de espera (T)')
plt.xlabel('T [s]')
plt.ylabel('ln(P) [ln(Hz)]')
#plt.axis([0, 19,0,6300])
plt.legend()
plt.show()

#print(plt.style.available)