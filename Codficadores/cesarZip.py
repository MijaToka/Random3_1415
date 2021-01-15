import rotn as r

def cesarZip(shift,code):
    cypher = ''

    for char in code:
        
        cypher += r.rotn(shift,char)
        
    
    return cypher


print(cesarZip(int(input()),input()), end='')
