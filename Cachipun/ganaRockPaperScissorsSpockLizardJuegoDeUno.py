import jugada as j
import random as r

def ganaRockPaperScissorsSpockLizardJuegoDeUno(rps):
    
    p = j.jugada2(rps)
    rand = r.randint(0,4)
    cp = j.jugada2(rand)
    
    if rps >= 5:
        game = 'Computador gana por default'
    
    elif rand == (rps + 1 )% 5 or rand == (rps + 3) % 5:
        game = 'Gana computador'
    
    elif rps == (rand + 1 )% 5 or rps == (rand + 3) % 5:
        game = 'Gana jugador'
    elif p == cp:
        game = 'Empate'
        
    print('Ud jugó ' + str(p))
    print('Computador jugó ' + str(cp))
    print(game)
#rps=3      #(si quiero hacelo repetidas veces)
rps = int(input('Ingrese 0 (piedra), 1 (papel), 2 (tijeras), 3 (Spock) o  4 (Lagarto) '))
ganaRockPaperScissorsSpockLizardJuegoDeUno(rps)