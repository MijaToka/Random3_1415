def mousse(n):
    if n == 0:
        huevos = 0
    else:
        huevos = n + 1
    azucar = n
    chocolat = n * 25
   
    print('Necesitas:')
    print('-' + str(huevos) +' huevos')
    print('-' + str(azucar) + ' cucharadas de azúcar')
    print('-' + str(chocolat) + 'g de chocolate negro')
   
n= int(input('¿Cuantas porciones de mousse quieres hacer? '))
mousse(n)
