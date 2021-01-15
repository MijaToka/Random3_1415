def decriptBible(shifts,string):
    cypher = ''
    for i in range(len(string)):
        if ord(string[i])>=ord('A') and ord(string[i])<=ord('Z'):
               
            cypher += chr((ord(string[i]) - ord('A') - shifts[i % len(shifts)] + 26) % 26 + ord('A'))
            
        elif ord(string[i])>=ord('a') and ord(string[i])<=ord('z'):
   
             cypher += chr((ord(string[i]) - ord('a') - shifts[i % len(shifts)] + 26) % 26 + ord('a'))
     
        else:
            
            cypher += string[i]
    
    return cypher

shiftString = input('Lista llave: ')   # Toma toda una línea de n números
shifts = list(map(int,shiftString.split(' ')))
string = input('Texto a desencriptar: ')
print(decriptBible(shifts,string), end='')