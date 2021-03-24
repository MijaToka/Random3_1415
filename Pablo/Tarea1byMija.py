
#import random as r
#Debido a que los numeros en español se nombran de a grupos de 1000
#Hago una funcion que nombre los números en este orden

def numeros1000(num,sobreMil = False):
    
    assert num < 1000 and num >= 0, 'Input fuera del rango aceptado (0 a 999)'
    #Casos especiales
    if num == 0:
        return 'cero'
    
    if num == 1 and not sobreMil:
        return 'uno'

    if num == 100:
        return 'cien'

    (c,d,u) = num//100, (num//10)%10 , num%10

    unidades = ["cero","un","dos","tres","cuatro","cinco","seis","siete","ocho",
              "nueve"]
    decenas = ["","diez","veinte","treinta","cuarenta","cincuenta","sesenta",
             "setenta","ochenta","noventa"]
    centenas = ["","ciento","doscientos","trescientos","cuatrocientos","quinientos",
              "seiscientos","setecientos","ochocientos","novecientos"]
    
    #Como en español los numeros del 11 al 29 son una palabra compuesta y no palabras adjuntas
    #Hay que escribirlo com casos particulares

    onceAlVeintinueve = {11:"once", 12:"doce", 13:"trece", 14:"catorce", 15:"quince", 16:"dieciséis",
                         17:"diecisiete", 18:"dieciocho", 19:"diecinueve", 20:"veinte", 21:"veintiun",
                         22:"veintidós", 23:"veintitrés", 24:"veinticuatro", 25:"veinticinco", 26:"veintiséis",
                         27:"veintisiete", 28:"veintiocho", 29:"veintinueve"}
    
    #Luego hay que unirlos
    if 0 < num and num < 10:
        return unidades[num]

    if (d == 1 and u != 0) or d == 2:
        palabras = (centenas[c] + ' ')  * (c!=0) + \
                    onceAlVeintinueve[d*10 + u] + ('o') * (d*10 + u == 21 and not sobreMil)
    else:
        palabras =  (centenas[c] + ' ')  * (c!=0) + \
                    (decenas[d]) + \
                    (' y ') * ((u!=0) and (d!=0)) + \
                    (unidades[u]) * (u!=0) + 'o' * (u == 1 and not sobreMil)

    return palabras 

# for i in range(1000):
#     print(numeros1000(i,sobreMil=True))

def Numeros(num):

    assert 0 < num and num < 10**9, 'Input fuera del rango aceptado (0 a 10**9)'

    #Casos especiales
    if num == 0:
        return 'cero'
    if num == 1000:
        return 'mil'
    if num == 10**9:
        return 'mil millones'

    (millones,miles,unidades) = num//(10**6),num//(10**3)%10**3,num%10**3
    
    palabras =  (numeros1000(millones,sobreMil=True) + ' millon' + ('es')*(millones%10 != 1) + ' ') * (millones != 0) +\
                ((numeros1000(miles,sobreMil=True) + ' ') * (miles != 1) + 'mil ') * (miles != 0) + \
                numeros1000(unidades)

    return palabras


# for _ in range(10):
#     num = r.randint(0,(10**9) - 1)
#     print(Numeros(num))
# print(Numeros(101001011))

print(Numeros(int(input('Inserte el numero que para escribir (sin puntos ni espacios)\n'))))
input('')