class Cola:
    def __init__(self,n):
        self.__elementos = []
        self.__maxLen = n
    
    def vacia(self):
        return self.__elementos == []
    
    def largo(self):
        return len(self.__elementos)

    def largoMax(self):
        return self.__maxLen

    def llena(self):
        return self.largo() == self.__maxLen

    def poner(self,x):
        if not self.llena():
            self.__elementos.append(x)
    
    def sacar(self):
        if not self.vacia():
            return self.__elementos.pop(0)
        return []

    def vaciar(self):
        self.__elementos = []

    def valores(self):
        elementos = ''
        for elem in self.__elementos:
            elementos += str(elem) + ' '
        return elementos[:-1]

    
    
##TESTS
def test(Clase):
    C = Clase()
    C.poner('hola')
    assert not C.vacia()
    C.poner('que tal')
    print(C.sacar())
    print(C.sacar())
    print(C.elementos)
    assert C.vacia()
#test(Cola)

##PROGRAMA
def start():
    C = Cola(5)
    A,B = 1,100 + 1
    for i in range(A,B):
        C.poner(i)
    for _ in range(A,B):
        print(C.sacar())
#start()