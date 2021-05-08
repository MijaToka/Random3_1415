##Calculo de propagación de errores
import math as math

class Valores:
    def __init__(self,valor,error,unidad=''):
        self.valor=valor
        self.error=abs(error)
        self.unidad=unidad

    def __str__(self):
        return str(self.valor)+' '+chr(177)+' '+str(self.error)+" "+self.unidad

    def __add__(self,other):
        
        valor = self.valor + other.valor
        error = math.sqrt( (self.error)*(self.error) + (other.error)*(other.error) )
        unidad = self.unidad * (self.unidad == other.unidad)

        return Valores(valor,error,unidad)

    def __iadd__(self,other):
        return self.__add__(other)

    def __sub__(self,other):

        valor = self.valor - other.valor
        error = math.sqrt( (self.error)*(self.error) + (other.error)*(other.error) )
        unidad = self.unidad * (self.unidad == other.unidad)

        return Valores(valor,error,unidad)

    def __isub__(self,other):
        return self.__sub__(other)

    def __mul__(self,other):

        if type(other) == Valores:
            valor = self.valor * other.valor
            error = math.sqrt( (self.error/self.valor)**2 + (other.error/other.valor)**2 )
            unidad = self.unidad * (self.unidad == other.unidad)

            return Valores(valor,error,unidad)
        
        if type(other) == int or type(other) == float:
            
            return Valores(self.valor * other, self.error * other ,self.unidad)

    def __imul__(self,other):
        return self.__mul__(other)

    def __truediv__(self,other):

        assert type(other) == Valores

        valor = self.valor / other.valor
        error = math.sqrt( (self.error/self.valor)**2 + (other.error/other.valor)**2 )
        unidad = self.unidad * (self.unidad == other.unidad)

        return Valores(valor,error,unidad)

    def __itruediv__(self,other):
        return self.__truediv__(other)

    def __pow__(self,n):

        valor = self.valor ** n
        error = abs(n * (self.valor ** (n-1) ) * self.error)

        return Valores(valor,error,self.unidad)

    def __ipow__(self,n):
        return self._pow__(n)   

## Definicion de variavles

tolerancia = 0.01

C1 = Valores(2.2, 2.2 * tolerancia, "μF")
C2 = Valores(4.7, 4.7 * tolerancia, "μF")
C3 = Valores(5.6, 5.6 * tolerancia, "μF")

## Circuito 1 (3 Paralelo)
# Sabemos que para un circuito en paralelo la Capacitancia equivalente es la suma de capacitancias

Ceq1 = C1 + C2 + C3

print(f"Ceq circuito 3 serie: {Ceq1}")

## Circuito 2 (3 Serie)
# Sabemos que el Ceq de un circuito en serie esta dado por la siguiente relacion
#   	El inverso de Ceq equivale a la suma de los inversos

Ceq2 = (C1**(-1) + C2**(-1) + C3**(-1))**(-1)

print(f"Ceq circuito 3 paralelo: {Ceq2}")

## Circuito 3 (2 paralelo y 1 en serie)
# Aplicando las relaciones anteriores podemos primero reemplazar la parte en paralelo (C2 y C3) por un Ceq_2_3
# Quedando así un circuito en serie (C1 y Ceq_2_3)

Ceq3_2_3 = C2 + C3
Ceq3 = ( C1**(-1) + Ceq3_2_3**(-1) )**(-1)

print(f"Ceq circuito 2 paralelo y 1 serie: {Ceq3}")

## Circuito 4 (2 Serie y 1 Paralelo)
# De la misma manera que en el anterior pero invertido
# Primero reemplazar los 2 en serie (C2 y C3) por un Ceq_2_3
# Luego queda un circuito en paralelo (C1 y Ceq_2_3)

Ceq4_2_3 = ( C2**(-1) + C3**(-1) )**(-1)
Ceq4 = C1 + Ceq4_2_3

print(f"Ceq circuito 2 serie y 1 paralelo: {Ceq4}")