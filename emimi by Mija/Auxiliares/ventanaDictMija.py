#crear diccionario con datos de archivo “diccionario.txt”
from Diccionario import Diccionario
D=Diccionario()
#métodos para botones 
from tkinter import *  
def responder(x): respuesta.config(text=x)
def buscar():
  s=D.buscar(palabra.get())
  if s==None:
    responder("no existe")
  else:
    significado.delete(0,END) #limpiar
    significado.insert(0,s)
    responder("encontrada")
def agregar():
  if D.agregar(palabra.get(),significado.get()):
    responder("agregada")
  else: 
    responder("ya existe")
# def borrar():
#   if D.borrar(palabra.get()):
#     responder("borrada")
#   else: 
#     responder("no existe") 
# def cambiar():
#   if D.cambiar(palabra.get(),significado.get()):
#     responder("cambiado")
#   else: 
#     responder("no existe")
# def grabar():
#   D.grabar()
#   responder("grabado")  

#definir ventana con sus componentes
v=Tk()
titulo=Label(v,text="operaciones en diccionario")
operacion=Label(v,text='dar click en operación')
respuesta=Label(v,text="mensaje según operación")
f1=Frame(v); f2=Frame(v); f3=Frame(v)

#diagramar frames con palabra y significado
W=15
Label(f1,text="palabra:",width=W).pack(side=LEFT)
palabra=Entry(f1,width=W); palabra.pack()
Label(f2,text="significado:",width=W).pack(side=LEFT)
significado=Entry(f2,width=W); significado.pack()

#diagramar frame con botones
Button(f3,text="agregar",command=agregar).pack(side=LEFT)
Button(f3,text="buscar",command=buscar).pack(side=LEFT)
#Button(f3,text="borrar",command=borrar).pack(side=LEFT)
#Button(f3,text="cambiar",command=cambiar).pack(side=LEFT)
#Button(f3,text="grabar",command=grabar).pack(side=LEFT)

#diagramar y mostrar ventana
titulo.pack()
f3.pack()
operacion.pack()
f1.pack(); f2.pack()
respuesta.pack()
v.mainloop()



