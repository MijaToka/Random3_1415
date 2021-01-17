import random as rand

#Variables

DIRECTORIO = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Random/'
CHAMPS = DIRECTORIO + 'champs.txt'
ITEMS = DIRECTORIO + 'mythicItems.txt'
ROLES = ['Top','Jungle','Mid','Bot','Support']

#Function(s)

def lineLst(dir):
    '''Saves the contents of a file in a list which elements are the lines of the  file'''

    file = open(dir, 'r')
    lst = []
    for line in file:
        lst.append(line.strip())
    
    return lst

#Program

champLst = lineLst(CHAMPS)
itemLst = lineLst(ITEMS); rand.shuffle(itemLst)
rand.shuffle(ROLES)

print('Ingrese Jugadores')

playerLst = []
for _ in range(5):
    player = input('')
    if player == '': break
    playerLst.append(player)
print('')

n_players = len(playerLst)

pickedChamps = rand.sample(champLst,n_players)
pickedItems = itemLst[:n_players]
pickedRoles = ROLES[:n_players]

for i,_ in enumerate(playerLst):
    print(f'{playerLst[i]}: {pickedChamps[i]} rushing {pickedItems[i]} in {pickedRoles[i]}')

input('\nPresione Enter para salir')