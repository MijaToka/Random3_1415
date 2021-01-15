#__numerador : int
#__denominador : int
class Fraccion:
  def __init__(self,x,y): 
    self.__numerador=x; self.__denominador=y
  def __str__(self):
    return str(self.__numerador)+'/'+str(self.__denominador)
  def __add__(self,x): 
    assert isinstance(x,Fraccion) 
    num=self.__numerador * x.__denominador + \
        self.__denominador * x.__numerador
    den=self.__denominador * x.__denominador
    return Fraccion(num,den)
  def comparar(self,x): 
    assert isinstance(x,Fraccion) #x es Fraccion?
    return self.__numerador * x.__denominador   - \
           self.__denominador * x.__numerador
  def __gt__(self,x):
    return self.comparar(x)>0
  def __lt__(self,x):
    return self.comparar(x)<0
  def __eq__(self,x):
    return self.comparar(x)==0
  #__ladd__: Fraccion ->
  #sumar x a self
  #ej: f1 += f2
  def __ladd__(self,x): 
    assert isinstance(x,Fraccion) 
    num=self.__numerador * x.__denominador + \
        self.__denominador * x.__numerador
    den=self.__denominador * x.__denominador
    self.__numerador=num
    self.__denominador=den
  def __sub__(self,x): 
    assert isinstance(x,Fraccion) 
    num=self.__numerador * x.__denominador - \
        self.__denominador * x.__numerador
    den=self.__denominador * x.__denominador
    return Fraccion(num,den)

  def __mul__(self,x):
    assert isinstance(x,Fraccion) 
    num = self.__numerador * x.__numerador
    den = self.__denominador * x.__denominador
    return Fraccion(num,den)

  def __div__(self,x):
    assert isinstance(x,Fraccion) 
    num = self.__numerador * x.__denominador
    den = self.__denominador * x.__numerador
    return Fraccion(num,den)
#test de clase Fraccion
f1=Fraccion(1,2)
assert str(f1)=='1/2'
f2=Fraccion(1,3)
assert f1 > f2
assert f2 < f1
assert f1+f2 == Fraccion(5,6)
f1 += f2
assert f1 == Fraccion(5,6)



