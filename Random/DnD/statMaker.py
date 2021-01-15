#VARIABLES

DIRECTORIO_CHAR = 'C:/Users/Admin/Desktop/Computación herramientas/Progra/Archivos/py/Random/DnD/Character Sheets/'

PROFICIENCY = {





    
}
#FUNCTIONS & CLASSES

class Personaje:
    def __init__(self, Name, Race, Class, Background, Alignment, InitialStats):
        self.Name = Name
        self.Race = Race
        self.Class = Class
        self.Background = Background
        self.Alignment = Alignment
        self.str, self.dex, self.con, self.int, self.wiz, self.car = InitialStats
        self.modifiers()

    def setStat(self,str=None,dex=None,con=None,int=None,wiz=None,car=None):
        if not str==None: self.str = str
        if not dex==None: self.dex = dex
        if not con==None: self.con = con
        if not int==None: self.int = int
        if not wiz==None: self.wiz = wiz
        if not car==None: self.car = car
        return

    def upgradeStats(self,str=None,dex=None,con=None,int=None,wiz=None,car=None):
        currentStats = (self.str, self.dex, self.con, self.int, self.wiz, self.car)
        
        if not str==None: self.setStat(str=currentStats[0]+str)
        if not dex==None: self.setStat(dex=currentStats[1]+dex)
        if not con==None: self.setStat(con=currentStats[2]+con)
        if not int==None: self.setStat(int=currentStats[3]+int)
        if not wiz==None: self.setStat(wiz=currentStats[4]+wiz)
        if not car==None: self.setStat(car=currentStats[5]+car)
        return

    def modifiers(self):
        self.strMod = (self.str - 10)//2
        self.dexMod = (self.dex - 10)//2
        self.conMod = (self.con - 10)//2
        self.intMod = (self.int - 10)//2
        self.wizMod = (self.wiz - 10)//2
        self.carMod = (self.car - 10)//2
        return

#MAIN
Mija = Personaje('Mija','Humano','Artificer', 'Rich born', 'Neutral Good', (10,13,9,15,14,11))
Mija.upgradeStats(int=0)
print(Mija.Name)
print(Mija.Race)
print(Mija.Class)
print(Mija.Background)
print(Mija.Alignment)
print(Mija.str,Mija.strMod)
print(Mija.dex,Mija.dexMod)
print(Mija.con,Mija.conMod)
print(Mija.int,Mija.intMod)
print(Mija.wiz,Mija.wizMod)
print(Mija.car,Mija.carMod)

