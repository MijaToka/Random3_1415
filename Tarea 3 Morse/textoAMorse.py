#%%DICCIONARIO MORSE
diccionarioMorse = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', '~N':'--.--',
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
# Adaptado desde https://www.geeksforgeeks.org/morse-code-translator-python/, 
# agregando el código para el carácter ~N definido en https://es.wikipedia.org/wiki/C%C3%B3digo_morse

#%%FUNCIONES
def textoAMorse(t,d):
  morse = ''
  for char in t:
    if char in d:
      morse +=' ' + d[char]
    else:
      morse += ' '
  return morse[1:]

#%%MAIN
print(textoAMorse(input().upper(),diccionarioMorse),end='')

#%%