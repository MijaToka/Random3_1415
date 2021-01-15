from FraccionConOperadores import Fraccion

# def sub(self,x): 
#     assert isinstance(x,Fraccion) 
#     num=self.__numerador * x.__denominador - \
#         self.__denominador * x.__numerador
#     den=self.__denominador * x.__denominador
#     return Fraccion(num,den)

# def mul(self,x):
#     assert isinstance(x,Fraccion) 
#     num = self.__numerador * x.__numerador
#     den = self.__denominador * x.__denominador
#     return Fraccion(num,den)

# def div(self,x):
#     assert isinstance(x,Fraccion) 
#     num = self.__numerador * x.__denominador
#     den = self.__denominador * x.__numerador
#     return Fraccion(num,den)

# Fraccion.__sub__ = sub
# Fraccion.__mul__ = mul
# Fraccion.__div__ = div

#Main

def main():
    operators = {'+' : lambda x,y:x+y,
                 '-' : lambda x,y:x-y,
                 '*' : lambda x,y:x*y,
                 '/' :lambda x,y:x/y}
    print('Calculadora de Fracciones a/b y c/d')
    a = int(input('a? ')); b = int(input('b? '))
    c = int(input('c? ')); d = int(input('d? '))
    o = input('Operación (+ - * /)? ')
    out = operators[o](Fraccion(a,b),Fraccion(c,d))
    print(out)
main()