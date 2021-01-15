def rotn(shift,char):
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
               
        newchar = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        return newchar 
            
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
   
        newchar = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        return newchar
     
    else:
            
        return char
    
def desrotn(shift,char):
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
               
        newchar = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
        return newchar 
            
    elif ord(char)>=ord('a') and ord(char)<=ord('z'):
   
        newchar = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
        return newchar
     
    else:
            
        return char