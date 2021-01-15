def rot13Char(char):
    if char >= 'a' and char <= 'z':
        return chr(( ord(char) - ord('a') + 13 )%26 + ord('a'))
    if char >= 'A' and char <= 'Z':
        return chr(( ord(char) - ord('A') + 13 )%26 + ord('A'))
    else:
        return char

def rot13(string):
    cypher = ''
    for char in string:
        cypher += rot13Char(char)
    return cypher

def rot13_archivo(input,output):
    input_file = open(input,'r')
    output_file =open(output,'w')
    for line in input_file:
        output_file.write(rot13(line))
    input_file.close()
    output_file.close()
    return

inDir = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/EjerciciosFormativos/textfiles/input.txt'
in2Dir = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/EjerciciosFormativos/textfiles/input2.txt'
outDir = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/EjerciciosFormativos/textfiles/output.txt'

rot13_archivo(inDir,outDir)
rot13_archivo(outDir,in2Dir)