from tkinter import Tk, Label, Button, Entry

class ItemType:
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

    def compact(self):
        for i,_ in enumerate(self.__amounts):
            if i == len(self.__amounts) - 1:
                return self.__amounts
            if self.__amounts[i]<0:
                self.__amounts[i]*= -1
                self.__amounts[i+1] -= self.__amounts[i]//3
                self.__amounts[i] -= self.__amounts[i]//3 * 3
                self.__amounts[i]*= -1

def test():
    testItem =  ItemType('Slime', 3)
    testItem.addAmount(-35,1)
    testItem.addAmount(5,3)
    testItem.addAmount(1,2)
    print(testItem.getAmount())
    print(testItem.getTierOneAmount())
    testItem.compact()
    print(testItem.getAmount())
    print(testItem.getTierOneAmount())
test()

##VARIABLES

CHARACTERS = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Random/genshin Characters.txt'

#Crear diccionario de personajes
file = open(CHARACTERS,'r')
dictChar = {}
for line in file:
    items = line.strip().split(';')
    dictChar[items[0]] = items[1:]
file.close()

#Materiales de ascención

ASC1 = [(1,1), ( 0,1), ( 3,1), ( 3,1)]
ASC2 = [(3,2), ( 2,1), (10,1), (15,1)]
ASC3 = [(6,2), ( 4,1), (20,1), (12,2)]
ASC4 = [(3,3), ( 8,1), (30,1), (18,2)]
ASC5 = [(6,3), (12,1), (45,1), (12,3)]
ASC6 = [(6,4), (20,1), (60,1), (24,3)]

ASC = [ASC1,ASC2,ASC3,ASC4,ASC5,ASC6]

#Materiales para Talentos

TALENT_LVL1 = [( 0,1),( 0,1)]
TALENT_LVL2 = [( 3,1),( 6,1)]
TALENT_LVL3 = [( 2,2),( 3,2)]
TALENT_LVL4 = [( 4,2),( 4,2)]
TALENT_LVL5 = [( 6,2),( 6,2)]
TALENT_LVL6 = [( 9,2),( 9,2)]
TALENT_LVL7 = [( 4,3),( 4,3)]
TALENT_LVL8 = [( 6,3),( 6,3)]
TALENT_LVL9 = [(12,3),( 9,3)]
TALENT_LVL10= [(16,3),(12,3)]


TALENT_LVL_UP = [TALENT_LVL1, TALENT_LVL2,
                TALENT_LVL3, TALENT_LVL4,
                TALENT_LVL5, TALENT_LVL6,
                TALENT_LVL7,TALENT_LVL8,
                TALENT_LVL9,TALENT_LVL10]

##Ventana
#crear ventana
ventana = Tk()
ventana.title('Genshin Impact Item Calcualtor')

#Crear elementos
Personaje = Button(ventana, text='Insert')
Calcular = Button(ventana, text='Calculate')

Nombre = Label(ventana, text='Character Name')
Ascension = Label(ventana, text= 'Current Ascension Level')
Basic_Attack = Label(ventana, text = 'Basic Attack Level')
Ability = Label(ventana, text = 'Elemental Ability Level')
Burst = Label(ventana, text = 'Elemental Burst Level')
Gem = Label(ventana, text = 'Gem')
Boss = Label(ventana, text = 'Boss Drop')
Speciality = Label(ventana, text = 'Local Speciality')
Common = Label(ventana, text = 'Common Material')
Book = Label(ventana, text = 'Talen-up Material')
From1 = Label(ventana, text = 'from')
From2 = Label(ventana, text = 'from')
From3 = Label(ventana, text = 'from')
To1 = Label(ventana, text = 'to')
To2 = Label(ventana, text = 'to')
To3 = Label(ventana, text = 'to')
Tier101 = Label(ventana, text = 'tier 1')
Tier102 = Label(ventana, text = 'tier 1')
Tier103 = Label(ventana, text = 'tier 1')
Tier201 = Label(ventana, text = 'tier 2')
Tier202 = Label(ventana, text = 'tier 2')
Tier203 = Label(ventana, text = 'tier 2')
Tier301 = Label(ventana, text = 'tier 3')
Tier302 = Label(ventana, text = 'tier 3')
Tier303 = Label(ventana, text = 'tier 3')
Tier4 = Label(ventana, text = 'tier 4')
ResultGemt1 = Label(ventana, text='')
ResultGemt2 = Label(ventana, text='')
ResultGemt3 = Label(ventana, text='')
ResultGemt4 = Label(ventana, text='')
ResultBoss = Label(ventana, text='')
ResultSpeciality = Label(ventana, text='')
ResultCommon = Label(ventana, text='')
ResultBook = Label(ventana, text='')

NameEntry = Entry(ventana)
Asc = Entry(ventana)
AAfrom = Entry(ventana)
AAto = Entry(ventana)
ESfrom = Entry(ventana)
ESto = Entry(ventana)
EBfrom = Entry(ventana)
EBto = Entry(ventana)
Tier101Entry = Entry(ventana)
Tier102Entry = Entry(ventana)
Tier103Entry = Entry(ventana)
Tier201Entry = Entry(ventana)
Tier202Entry = Entry(ventana)
Tier203Entry = Entry(ventana)
Tier301Entry = Entry(ventana)
Tier302Entry = Entry(ventana)
Tier303Entry = Entry(ventana)
Tier4Entry = Entry(ventana)

#Diagramar Ventana
Nombre.grid(row = 0,column=0,rowspan=1,columnspan=2)
NameEntry.grid(row = 0,column=2,rowspan=1,columnspan=6)
Ascension.grid(row = 0,column=8,rowspan=1,columnspan=2)
Asc.grid(row = 0,column=10,rowspan=1,columnspan=6)
Personaje.grid(row = 0,column=16,rowspan=1,columnspan=8)
Basic_Attack.grid(row = 1,column=0,rowspan=1,columnspan=2)

From1.grid(row = 1,column=2,rowspan=1,columnspan=1)
AAfrom.grid(row = 1,column=3,rowspan=1,columnspan=2)
To1.grid(row = 1,column=5,rowspan=1,columnspan=1)
AAto.grid(row = 1,column=6,rowspan=1,columnspan=2)
Ability.grid(row = 1,column=8,rowspan=1,columnspan=2)
From2.grid(row = 1,column=10,rowspan=1,columnspan=1)
ESfrom.grid(row = 1,column=11,rowspan=1,columnspan=2)
To2.grid(row = 1,column=13,rowspan=1,columnspan=1)
ESto.grid(row = 1,column=14,rowspan=1,columnspan=2)
Burst.grid(row = 1,column=16,rowspan=1,columnspan=2)
From2.grid(row = 1,column=18,rowspan=1,columnspan=1)
EBfrom.grid(row = 1,column=19,rowspan=1,columnspan=2)
To2.grid(row = 1,column=21,rowspan=1,columnspan=1)
EBto.grid(row = 1,column=22,rowspan=1,columnspan=2)

Gem.grid(row = 2,column=0,rowspan=1,columnspan=3)





ventana.mainloop()