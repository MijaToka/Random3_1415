from tkinter import Tk, Label, Button, Entry
import Cola as C

#Crea la cola de max 5 personas
Cola = C.Cola(5)

#metodos que se ejecutan al clickear botones 
def llegando():
    if not Cola.llena():#Cuando llegan personas
        persona = llega.get()
        
        Cola.poner(persona)
        enCola.config(text=Cola.valores())
        cupos.config(text=str(Cola.largoMax()-Cola.largo()))
        
        llega.delete(0,len(persona))

        if Cola.vacia():
            estado.config(text='Vacia')
        else:
            estado.config(text='Ok')

def atender():
    if not Cola.vacia():

        primero = Cola.sacar()
        enCaja.config(text=str(primero))
        enCola.config(text=Cola.valores())
        cupos.config(text=str(Cola.largoMax()-Cola.largo()))

        if Cola.vacia():
            estado.config(text='Vacia')
        else:
            estado.config(text='Ok')

    else:
        enCaja.config(text='')
        cupos.config(text=str(Cola.largoMax()-Cola.largo()))

#crear ventana
ventana = Tk()
ventana.title('Cola Caja')
#definir componentes
botonAtender = Button(ventana,text='Atender',command=atender)
enCaja = Label(ventana)
enCola = Label(ventana)
cupos = Label(ventana,text=str(Cola.largoMax()-Cola.largo()))
estado = Label(ventana,text='Vacia')

llega = Entry(ventana)

txtBoton = Label(ventana,text='Caja',width=10)
txtenCaja = Label(ventana,text='en Caja',width=10)
txtenCola = Label(ventana,text='en Cola',width=15)
txtcupos = Label(ventana,text='Cupos',width=5)
txtllega = Label(ventana,text='LLega',width=15)
txtEstado = Label(ventana,text='Estado',width=10)

actualizar = Button(ventana,text= 'Entrar',command=llegando)

#diagramar ventana
txtBoton.grid(row=0,column=0)
txtenCaja.grid(row=0,column=1)
txtenCola.grid(row=0,column=2)
txtcupos.grid(row=0,column=3)
txtllega.grid(row=0,column=4)
txtEstado.grid(row=0,column=6)

botonAtender.grid(row=1,column=0)
enCaja.grid(row=1,column=1)
enCola.grid(row=1,column=2)
cupos.grid(row=1,column=3)
llega.grid(row=1,column=4)
estado.grid(row=1,column=6)

actualizar.grid(row=1,column=5)
#mostrar ventana (hasta que se cierre)

ventana.mainloop()
