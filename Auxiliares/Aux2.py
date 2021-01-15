import math
def SolucionEcuacion(a,b,c):
    '''Resuelve ecuaciones del tipo a*x^2+b*x+c = 0'''
    if a == 0:
        if b == 0:
            return 'Undefined'
        else:
            x = -c/b
            return x
    else:
        d = (b**2) - (4*a*c)
        if d == 0:
            x = -b/(2*a)
            return x
        elif d > 0:
            x = [(-b + math.sqrt(d)) / (2*a) ,
                 (-b - math.sqrt(d)) / (2*a)]
            return x
        elif d < 0: 
            return 'Complex solutions'

def SolucionInteractiva():
    print('Desea resolver una ecuacion de tipo a*x^2 + b*x + c = 0')
    while True:
        
        a = float(input('a: '))
        b = float(input('b: '))
        c = float(input('c: '))     
        
        print(SolucionEcuacion(a,b,c))
        
        r = input('¿Desea resolver una ecuacion de tipo a*x^2 + b*x + c = 0?')
        
        if r.casefold() != 'si' or r.casefold() != 'yes':
            break
    
def InteresCompuesto(monto,interes,años):
    montoFinal = monto * (1 + (interes / 100))**años
    return montoFinal
