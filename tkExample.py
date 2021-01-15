from tkinter import Tk, Button,Label
#metodos que se ejecutan al clickear botones 
def saludar(): saludo.config(text="hola")
def greet(): saludo.config(text="hello")
#crear ventana
v = Tk()
#definir componentes
b1 = Button(v,text="español",command=saludar)
b2 = Button(v,text="english",command=greet)
saludo = Label(v)
#diagramar ventana
b1.pack()     #b1 arriba
b2.pack()     #b2 debajo de anterior
saludo.pack() #saludo abajo
#mostrar ventana (hasta que se cierre)
v.mainloop()
