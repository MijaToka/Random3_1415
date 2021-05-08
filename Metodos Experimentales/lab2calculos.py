import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#%%Calculos

DIR = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Metodos Experimentales/'

L = 0.65

datos = pd.read_excel(DIR+'Lab Regresion sin Calculos.xlsx')

xi = datos['n']
yi = datos['f']

xiyi,xi2 = [],[]

for i in range(len(xi)):

    xiyi.append(xi[i]*yi[i])
    xi2.append(xi[i]**2)

averageY = sum(yi)/len(yi)

a = (len(xi)*sum(xiyi) - sum(xi)*sum(yi)) / (len(xi)*sum(xi2) - sum(xi)**2)
b = (sum(yi)*sum(xi2) - sum(xiyi)*sum(xi)) / (len(xi)*sum(xi2) - sum(xi)**2)

y_estimado,chi,dPromedio2  = [],[],[]

for i in range(len(xi)):
    y_estimado.append(a * xi[i] + b)
    chi.append((a * xi[i] + b - yi[i])**2)
    dPromedio2.append((yi[i]-averageY)**2)

Error = (sum(chi)/(len(chi)-2))**0.5
Correlacion = 1 - sum(chi)/sum(dPromedio2)


#%% Grafico

x, y, yhat = np.array(xi), np.array(yi), np.array(y_estimado)

#plt.style.use(plt.style.available[7])
plt.plot(x,yhat,color='r',markersize=1,label='Regresión lineal')
plt.scatter(x,y,label='Frecuencias medidas')
plt.title('Frecuencia vs Modo')
plt.xlabel('Modo de vibración (n)')
plt.ylabel('Frecuencia [Hz]')
plt.axis([0, 19,0,6300])
plt.legend()
plt.show()

#print(plt.style.available)