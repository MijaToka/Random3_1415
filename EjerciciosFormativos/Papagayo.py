
def papagayo(string):
    if string.upper() == "HOLA!":
      print("Holi!")
    
    elif string == "Holi":
      print("Hola!")
    
    elif string.startswith('¿') and string.endswith('?'):
     string = string.replace('¿','¡')
     print((string.replace('?','!') + ' ')*3)
    
    elif string.startswith('Que tal') or string.startswith('Como estas'):
      print('Bien! '*3)

    elif string.casefold() == 'quieres algo de comer?':
      print('Quiero un plato de semillas!')
      print('Kwak!')
    elif string == '' or string.startswith('Chao')\
     or string.startswith('Adios'):
       return

    else:
      print(string+"!")

print("Kwak!")
while True:
    string = input()
    papagayo(string)
    if string == '' or string.startswith('Chao') \
    or string.startswith('Adios'):
      break
print("Ciao!")