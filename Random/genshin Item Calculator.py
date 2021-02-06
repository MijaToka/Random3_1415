
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

def datos(directorio):
    file = open(directorio,'r')
    dict = {}
    for line in file:
        items = line.strip().split(';')
        dict[items[0]] = items[1:]
    file.close()
    return dict  

dictChar = datos(CHARACTERS)

#PERSONAJE = input('Inserte nombre del personaje')

PERSONAJE = 'Xiao'

items = dictChar[PERSONAJE]

gem = itemType(items[0],4)
boss = itemType(items[1],1)
speciality = itemType(items[2],1)
common = itemType(items[3],3)
talent = itemType(item[4],3)

#Personaje de 1 -> 90
# tier of item = [gem, boss material, local spaciality, common material]

tiersAscencion = [[1,46,168,18],[9,0,0,30],[9,0,0,36],[6,0,0,0]]

#Tier talent material = [book,common material]
talentLvl = [[3,6],[21,22]]

charItems = [gem,boss,speciality,common,talent]

    for i,item in enumerate(charItems[:-1]):
        for tier in range(item.maxTier):
            item.addAmount()
