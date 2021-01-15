import leo

def listaCompra(combinaciones,pedido):
    
    listComb = combinaciones.split(';')
    listCompuestos = []
    for i in range(len(listComb)):
        colours = listComb[i].split('=')
        colour = colours[-1]
        listCompuestos += [colour]
    
    pedidoList = pedido.split(';')
    
    salida = ''
    
    for color in pedidoList:
        if color in listCompuestos:
            combinacion = leo.buscar_combinacion(combinaciones, color)
            sumIngredientes = combinacion.split('=')
            comb = sumIngredientes[0]
            ingredientes = comb.split('+')
            for ingrediente in ingredientes:
                salida = leo.agregar(salida,ingrediente)
        else:
            listaCompras = leo.agregar(salida,color)
            salida = listaCompras
    return salida[1:]
        
# combinaciones=input()
combinaciones="amarillo+rojo=naranja;azul+amarillo=verde;rojo+azul=violeta;azul+violeta=ultramar\
    ;azul+blanco=celeste;rojo+blanco=rosa;verde+amarillo=lima;blanco+negro=gris;amarillo+negro=marron\
    ;verde+azul=turquesa;violeta+blanco=magenta;negro+rojo=granate;naranja+negro=cafe;gris+negro=plomo"

#pedido = input()
pedido = 'amarillo;turquesa;verde;granate;plomo;rojo'

print(listaCompra(combinaciones,pedido))