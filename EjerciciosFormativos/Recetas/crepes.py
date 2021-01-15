import math as m
def crepes(cant):
    harina = int(cant / 15 * 250 * 100) / 100
    huevos = m.ceil(cant / 15 * 4)
    liquido = int(cant / 15 * 500 *100) / 100
    bicarbonato = int(cant / 15 * 5 *100) / 100
    sal = bicarbonato
    azucar = bicarbonato

    print('-' + str(harina) + 'g de harina')
    print('-' + str(huevos) + ' huevos (o equivalente)')
    print('-' + str(liquido) + 'cl de liquido (leche, cerveza, agua, etc)')
    print('-' + str(bicarbonato) + 'g de bicarbonato')
    print('-' + str(sal) + 'g de sal')
    print('-' + str(azucar) + 'g de azucar')
    
n= int(input('¿Cuantos crepes quieres hacer? '))
crepes(n)
