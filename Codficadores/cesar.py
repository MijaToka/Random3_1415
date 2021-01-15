#Encriptador
def cesar(shift,code):
    cypher = ''

    for char in code:
        if ord(char)>=ord('A') and ord(char)<=ord('Z'):
               
            cypher += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            
        elif ord(char)>=ord('a') and ord(char)<=ord('z'):
   
            cypher += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
     
        else:
            
            cypher += char
    
    return cypher

print(cesar(int(input()),input()), end='')

'''
shift = input()
code = input()
print(cesar(shift,code))
'''