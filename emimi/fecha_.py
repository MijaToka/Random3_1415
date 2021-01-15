#modulo fecha

#dia: int -> int
#dia de fecha de la forma DDMMAAAA
#ej: dia(18091810) -> 18
def dia(fecha): 
    assert type(fecha)==int and fecha>=0
    return fecha//1000000
assert dia(18091810)==18

#mes: int -> int
#mes de fecha de la forma DDMMAAAA
#ej: mes(18091810) -> 9
def mes(fecha): 
    assert type(fecha)==int and fecha>=0
    return fecha//10000%100
assert mes(18091810)==9

#año: int -> int
#año de fecha de la forma DDMMAAAA
#ej: año(18091810) -> 1810
def año(fecha): 
    assert type(fecha)==int and fecha>=0
    return fecha%10000
assert año(18091810)==1810

#bisiesto: int -> bool
#True si año x es bisiesto (False si no)
#ej: bisiesto(2019) -> False (no es divisible por 4)
#ej: bisiesto(2020) -> True  (divisible por 4)
#ej: bisiesto(1900) -> False (divisible por 100)
#ej: bisiesto(2000) -> True  (divisible por 400)
def bisiesto(x):
    assert type(x)==int and x>=0
    return x%4==0 and x%100!=0 or x%400==0
assert not bisiesto(2019)
assert bisiesto(2020)
assert not bisiesto(1900)
assert bisiesto(2000)
