def rot13(char):
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
        rank = ord(char) - ord('A')
        shiftedRank = (rank + 13) % 26
        newOrd = shiftedRank + ord('A')
        
        return chr(newOrd)
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
   
        rank = ord(char) - ord('a')
        shiftedRank = (rank + 13) % 26
        newOrd = shiftedRank + ord('a')
        return chr(newOrd)
     
    else:
        return char
    
