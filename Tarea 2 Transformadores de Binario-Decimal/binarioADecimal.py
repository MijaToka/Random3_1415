def sumandosBinarioADecimal(n2, n10 = '' ,n = 0):
  """Traduce una representacion binaria de un valor a su representacion decimal."""
  if n2 == '':
    return ''
  else:
    if int(n2) == 0 and n10 == '':
      return [0]
    elif int(n2) == 0:
      return 0
    else:
      n10 = 'a' 
      sumandos = list(sumandosBinarioADecimal(n2[:-1], n10, n+1)) +  [int(n2[-1]) * 2**n] 
      return list(sumandos)
  
def listSum(List):
  Sum = 0
  for i in range(len(List)):
    Sum += List[i]

  return Sum

def binarioADecimal(n2):
  """Traduce una representacion binaria de un valor a su representacion decimal."""
  sumandos = sumandosBinarioADecimal(n2)
  if sumandos == '':
    return ''
  else:
    suma = listSum(sumandos)
    return str(suma)

print(binarioADecimal(input()), end='')

def binarioADecimalInt(n2, i = 0):
  """Traduce una representacion binaria de un valor a su representacion decimal."""
  if len(n2) == 1:#Caso Base
    return 2**i * int(n2)
  elif n2 == '':#Caso Especial
      return ''
  else:#Caso Recursivo
    return binarioADecimalInt(n2[:-1], i+1)+ 2**i * int(n2[-1])

def binarioADecimal(n2):#Pasar de int() a str()
  return str(binarioADecimalInt(n2))