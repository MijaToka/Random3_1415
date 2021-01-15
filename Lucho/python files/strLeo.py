import leo

def listaCompra2(combinaciones,pedido):
    
    pedido += ';'
    
    i = 0 ; j = 0
    salida = ''
    while i<len(pedido):
        
        if pedido[i] == ';':
            color = pedido[j:i]
            
            combinacion = leo.buscar_combinacion(combinaciones,color)
            
            if combinacion == '': #Cuando es no compuesto
                salida = leo.agregar(salida,color)
                j = i + 1
            
            else: #Cuando es compuesto
                k = 0 ; l = 0
                while k < len(combinacion):
                    if combinacion[k] == '+' or combinacion[k] == '=':
                        ingrediente = combinacion[l:k]
                        salida = leo.agregar(salida,ingrediente)
                        l = k + 1
                        if combinacion[k] == '=':
                            pass
                    k += 1
                j = i + 1
        i += 1
        
    return salida[1:]

#combinaciones=input()
combinaciones="amarillo+rojo=naranja;azul+amarillo=verde;rojo+azul=violeta;azul+violeta=ultramar\
    ;azul+blanco=celeste;rojo+blanco=rosa;verde+amarillo=lima;blanco+negro=gris;amarillo+negro=marron\
    ;verde+azul=turquesa;violeta+blanco=magenta;negro+rojo=granate;naranja+negro=cafe;gris+negro=plomo"

#pedido = input()
pedido = 'amarillo;turquesa;verde;granate;plomo;rojo'

print(listaCompra2(combinaciones,pedido))