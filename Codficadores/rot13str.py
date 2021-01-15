def rot13str(string):
    cypher = ''
    for char in string:
        if ord(char)>=ord('A') and ord(char)<=ord('Z'):
            rank = ord(char) - ord('A')
            shiftedRank = (rank + 13) % 26
            newOrd = shiftedRank + ord('A')
        
            cypher += chr(newOrd)
        elif ord(char)>=ord('a') and ord(char)<=ord('z'):
   
            rank = ord(char) - ord('a')
            shiftedRank = (rank + 13) % 26
            newOrd = shiftedRank + ord('a')
            cypher += chr(newOrd)
     
        else:
            cypher += char
            
    return cypher

print(rot13str(input()), end='')