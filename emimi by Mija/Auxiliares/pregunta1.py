archivo = open('c:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/emimi by Mija/hola.txt','r')

nLineas = 0
nCaracteres = 0

for line in archivo:
    line.strip()
    nLineas += 1
    nCaracteres += len(line)

archivo.close()

print(f'Lineas = {nLineas}')
print(f'Caracteres = {nCaracteres-1}')