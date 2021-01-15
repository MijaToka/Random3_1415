import estructura
import math

estructura.crear('fraccion', 'numerador denominador')

def simplifica_fraccion(f):
  """Simplifica la fraccion _f_."""
  g = math.gcd(f.numerador,f.denominador)
  return fraccion(f.numerador/g,f.denominador/g)

assert simplifica_fraccion(fraccion(4,8)) == fraccion(1,2)

def suma_fracciones(f1,f2):
  """Suma dos fracciones definidas usando el modulo _estructura_."""
  assert type(f1) == fraccion and type(f2) == fraccion
  assert f1.denominador !=0 and f2.denominador !=0
  
  num = f1.numerador * f2.denominador + f1.denominador * f2.numerador
  den = f1.denominador * f2.denominador
  sum = fraccion(num,den)
  sumSimplificado = simplifica_fraccion(sum)
  return sumSimplificado

f1 = fraccion(1,2)
f2 = fraccion(3,4)
assert suma_fracciones(f1,f2) == fraccion(5,4)

def resta_fracciones(f1,f2):
  """Suma dos fracciones definidas usando el modulo _estructura_."""
  assert type(f1) == fraccion and type(f2) == fraccion
  assert f1.denominador !=0 and f2.denominador !=0
  
  num = f1.numerador * f2.denominador - f1.denominador * f2.numerador
  den = f1.denominador * f2.denominador
  sum = fraccion(num,den)
  sumSimplificado = simplifica_fraccion(sum)
  return sumSimplificado

f1 = fraccion(1,2)
f2 = fraccion(3,4)
assert resta_fracciones(f1,f2) == fraccion(-1,4)

def multiplica_fracciones(f1,f2):
  """Multiplica 2 fracciones usando el modulo__estructura__."""
  assert type(f1) == fraccion and type(f2) == fraccion
  assert f1.denominador !=0 and f2.denominador !=0

  num = f1.numerador * f2.numerador
  den = f1.denominador * f2.denominador

  prod = fraccion(num,den)

  return simplifica_fraccion(prod)

f1 = fraccion(1,2)
f2 = fraccion(3,4)
assert multiplica_fracciones(f1,f2) == fraccion(3,8)

def divide_fracciones(f1,f2):
  """Divide 2 fracciones usando el modulo__estructura__."""
  assert type(f1) == fraccion and type(f2) == fraccion
  assert f1.denominador !=0 and f2.denominador !=0 and f2.numerador != 0

  f2inv = fraccion(f2.denominador,f2.numerador)

  return multiplica_fracciones(f1,f2inv)

f1 = fraccion(1,2)
f2 = fraccion(3,4)
assert divide_fracciones(f1,f2) == fraccion(2,3)
