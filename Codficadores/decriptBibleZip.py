import rotn as r

def decriptBibleZip(shifts,string):
    cypher = ''
    for i in range(len(string)):
       
        cypher += r.desrotn(shifts[i % len(shifts)],string[i])
    
    return cypher

shiftString = input()   # Toma toda una línea de n números
shifts = list(map(int,shiftString.split(' ')))
string = input()
print(decriptBibleZip(shifts,string), end='')
