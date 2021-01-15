nombre = input('Nombre del archivo? ')

archivo = open(nombre,'r')

nLineas = 0
nCaracteres = 0

for line in archivo:
    line.strip()
    nLineas += 1
    nCaracteres += len(line)

archivo.close()

print(f'Lineas = {nLineas}')
print(f'Caracteres = {nCaracteres-1}')