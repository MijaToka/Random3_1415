import jugada as j
import random as r

def cachipun(rps):
    
    p = j.jugada(rps)
    rand = r.randint(0,2)
    cp = j.jugada(rand)
    
    if rps >= 3:
        game = 'Computador gana por default'
    
    elif rand == (rps + 1 )% 3:
        game = 'Gana computador'
    
    elif rps == (rand + 1 )% 3:
        game = 'Gana jugador'
    elif p == cp:
        game = 'Empate'
        
    print('Ud jugó ' + str(p))
    print('Computador jugó ' + str(cp))
    print(game)
#rps=2      #(si quiero hacelo repetidas veces)
rps = int(input('Ingrese 0 (piedra), 1 (papel) o 2 (tijeras) '))
cachipun(rps)