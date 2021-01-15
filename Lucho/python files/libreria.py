#VARIABLES

LIBRERIAS = {"Ateneo":  [("Ciencias;2ed",10000),("Papelucho;3ed",3000),("LyC;1ed",5000),("Historia;1ed",3000),("English;2ed",2000)],
            "Internacional":[("Ciencias;2ed",8000),("Papelucho;1ed",5000),("Historia;2ed",3000),("English;3ed",7500),("Matematica;1ed",9000)],
            "Nacional":[("LyC;2ed",4500),("Ciencias;1ed",9000),("Papelucho;2ed",6000),("Literatura;1ed",3000),("Historia;2ed",3500),("Matematica;2ed",9000)]}

#FUNCIONES

def buscarLibros(librerias, libro):
    precios = {}
    
    for libreria in librerias:
        for libroPrecio in librerias[libreria]:
            if libroPrecio[0].split(';')[0] == libro:
                precios[libreria] = libroPrecio[1]

    return precios

#print(buscarLibros(LIBRERIAS, 'LyC'))
# print(buscarLibros(LIBRERIAS, 'Biologia'))

def mejorOferta(preciosLibreria):
    if preciosLibreria == {}:
        return '', 0
    else:
        precios = list(preciosLibreria.values()); bestPrecio = precios[0]
        librerias = list(preciosLibreria.keys()); bestLibreria = librerias[0]

        for libreria in preciosLibreria:
            if bestPrecio > preciosLibreria[libreria]:
                bestPrecio = preciosLibreria[libreria]
                bestLibreria = libreria

        return bestLibreria,bestPrecio

#print(mejorOferta(buscarLibros(LIBRERIAS, 'LyC')))

def dondeComprar(librerias,librosLst):
    mejores = {}
    for libro in librosLst:
        preciosLibro = buscarLibros(librerias,libro)
        mejorPrecio = mejorOferta(preciosLibro)
        mejores[libro] = mejorPrecio

    return mejores

#print(dondeComprar(LIBRERIAS,["LyC", "Papelucho", "Matematica", "Biologia"]))

