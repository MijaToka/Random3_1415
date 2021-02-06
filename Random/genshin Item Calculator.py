
class itemType:
    def __init__(self,name,maxTier):
        self.name = name
        self.maxTier = maxTier
        self.__amounts = [0]*maxTier

    def addAmount(self,amount,tier):
        assert tier <= self.maxTier and tier > 0, 'Invalid tier.'
        self.__amounts[tier-1] += amount

    def getAmount(self):
        return self.__amounts

    def getTierOneAmount(self):
        amount = 0
        for i in range(self.maxTier):
            amount += self.__amounts[i] * 3**i 
        return amount


def test():
    testItem =  itemType('Slime', 3)
    testItem.addAmount(35,1)
    testItem.addAmount(5,3)
    testItem.addAmount(1,2)
    print(testItem.getAmount())
    print(testItem.getTierOneAmount())

CHARACTERS = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Random/genshin Characters.txt'

'''file = open(CHARACTERS,'r')
for line in file:

    assert len(line.strip().split(';')) == 5,line.strip().split(';')
    
file.close()'''


file = open(CHARACTERS,'r')
dictChar = {}
for line in file:
    items = line.strip().split(';')
    dictChar[items[0]] = items[1:]
file.close()


#PERSONAJE = input('Insert the name of the character (Capitalized)\n')

PERSONAJE = 'Xiao'
MAX_ASCENCION = 6

items = dictChar[PERSONAJE]

gem = itemType(items[0],4)
boss = itemType(items[1],1)
speciality = itemType(items[2],1)
common = itemType(items[3],3)
talent = itemType(items[4],3)

#Personaje de 1 -> 90
# tier of item = [gem, boss material, local speciality, common material]
ASC1 = [(1,1), (0,1),  (3,1),  (3,1) ]
ASC2 = [(3,2), (2,1),  (10,1), (15,1)]
ASC3 = [(6,2), (4,1),  (20,1), (12,2)]
ASC4 = [(3,3), (8,1),  (30,1), (18,2)]
ASC5 = [(6,3), (12,1), (45,1), (12,3)]
ASC6 = [(6,4), (20,1), (60,1), (24,3)]

ASC = [ASC1,ASC2,ASC3,ASC4,ASC5,ASC6]

#ASCENCION_ACTUAL = int(input(f'Current ascension level of {PERSONAJE}\n'))

ASCENCION_ACTUAL = 3

#Agregar los materiales necesarios para ascender ACTUAL -> 6

itemLst =  [gem, boss, speciality, common]
for i in range(ASCENCION_ACTUAL,MAX_ASCENCION): #Recorre ascenciones
    for j in range(len(itemLst)): #Recorre tipo de item
        '''
        ASC[i] := items de la ascencion i+1
        ASC[i][j] := #items j de la ascencion i+1 
        '''
        itemLst[j].addAmount(ASC[i][j][0] , ASC[i][j][1])


#talent lvl = [book, common material]
TALENT_LVL1 = [(0,1),(0,1)]
TALENT_LVL2 = [(3,1),(6,1)]
TALENT_LVL3 = [(2,2),(3,2)]
TALENT_LVL4 = [(4,2),(4,2)]
TALENT_LVL5 = [(6,2),(6,2)]
TALENT_LVL6 = [(9,2),(9,2)]

TALENT_LVL_UP = [TALENT_LVL1, TALENT_LVL2,
                TALENT_LVL3, TALENT_LVL4,
                TALENT_LVL5, TALENT_LVL6]


talentItemLst = [talent, common]

maxTalentLvl = 6

inputTxt = [' basic attacks', ' elemental ability', ' elemental burst']
for k in range(3):
    #talentLvl = int(input(f'Level of {PERSONAJE}'s {inputTxt[k]}\n'))
    talentLvl = 4
    for i in range(talentLvl,maxTalentLvl): #Recorre nivel del talento
        for j in range(len(talentItemLst)): #Recorre tipo de item
            '''
            TALENT_LVL_UP[i] := items del talento lvl i+1
            TALENT_LVL_UP[i][j] := #items j del talento lvl i+1 
            '''
            talentItemLst[j].addAmount(TALENT_LVL_UP[i][j][0],TALENT_LVL_UP[i][j][1])

#Luego restar la cantidad de items que el jugador ya posee
print(talent.getTierOneAmount(),gem.getAmount())
itemLst.append(talent)
'''
print('Insert the amount you have in your inventory of the folowing.')
for item in itemLst: #Recorre todos los items
    maxTier = item.maxTier
    if maxTier == 1:
        itemInventory = int(input(f'{item.name}: '))
        item.addAmount(itemInventory,1)
    else:
        for i in range(maxTier): #Recorre los tiers
            j=i+1 #Indica la cantidad de * del item
            if maxTier == 4:
                j+=1
            itemInventory = int(input(f'{j}star {item.name}: '))
            item.addAmount(itemInventory,i+1)
'''