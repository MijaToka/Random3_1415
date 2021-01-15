def base10ToBaseN(b10str,b=2):
  """Traduce una representacion decimal de un valor a su representacion en base n."""
  if b10str == '':#Caso vacio
    return ''
  b10 = int(b10str)
  div = b10//b
  mod = b10%b
  if div<b:#Caso base (Obs: cuando la primera entrada es < n, la salida será '0X')
    return str(int(str(div) + str(mod)))
  else:#Caso recursivo
    return base10ToBaseN(div,b) + str(mod)

print(base10ToBaseN(input()), end='')