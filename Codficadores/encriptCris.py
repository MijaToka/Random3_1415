import random
#chr(95) = a
#chr(122) = z
#chr(65) = A
#chr(90) = Z

def encriptar(texto):
    palabra = list(texto)
    key=random.randint(1,25)
    numbers=[]
    newnumbers=[]
    encriptado=""
    for elem in palabra:
        codigo=ord(elem)
        numbers.append(codigo)
    for num in numbers:
        if num in range(64, 123):
            num += key
            newnumbers.append(num)
        else:
            continue
    for new in newnumbers:
        encriptado += str(chr(new))
    return encriptado

def key(texto, encriptado):
    original = list(texto)
    nueva = list(encriptado)
    firstorig=ord(original[2])
    firstnueva=ord(nueva[2])
    key = firstnueva - firstorig

    return key

def desencriptar(key, encriptado):
    palabra = list(encriptado)
    numbers = []
    newnumbers = []
    desencriptado = ""
    for elem in palabra:
        codigo = ord(elem)
        numbers.append(codigo)
    for num in numbers:
        if num in range(64, 123):
            num -= key
            newnumbers.append(num)
        else:
            continue
    for new in newnumbers:
        desencriptado += str(chr(new))
    return desencriptado

texto = input("Ingrese un texto a cifrar: ")
encriptado = encriptar(texto)
key = key(texto, encriptado)
desencriptado = desencriptar(key, encriptado)

print(f"Encriptado: {encriptado}")
print(f"Key: {key}")
print(f"Desencriptado: {desencriptado}")

