from random import random
from tkinter import Tk, Button,Label
#metodos que se ejecutan al clickear botones 
def caraOsello():
    moneda = random()
    if moneda >= 0.5:
        return 'Cara'
    else:
        return 'Sello'
def tirarMoneda(): moneda.config(text = caraOsello())
#crear ventana
ventana = Tk()
#definir componentes
boton = Button(ventana,text='Cara o Sello',command=tirarMoneda)
moneda = Label(ventana)
#diagramar ventana
boton.pack()
moneda.pack()
#mostrar ventana (hasta que se cierre)
ventana.mainloop()

