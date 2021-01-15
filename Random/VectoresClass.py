from math import sqrt
class Vector:
    def __init__(self, lst):
        self.vector = lst

    def __str__(self):
        string = '['
        for elem in self.vector:
            string += str(elem) + ', '
        return string[:-2] + ']'

    def norma(self):
        return sqrt(self.__mul__(self))

    def __mul__(self,other):
        if type(other) == int or type(other) == float:
            V = Vector([])
            for vi in self.vector:
                V.vector.append(vi * other)
            return V

        elif type(other) == Vector:
            assert len(self.vector) == len(other.vector), 'Producto no definido'
            prod = 0
            for i in range(len(self.vector)):
                prod += self.vector[i]*other.vector[i]
            return prod
        pass

    def __add__(self,other):
        assert len(self.vector) == len(other.vector), 'Suma no definida'
        suma = Vector([])
        for i in range(len(self.vector)):
            suma.vector.append(self.vector[i] + other.vector[i])
        return suma

    def __sub__(self,other):
        assert len(self.vector) == len(other.vector), 'Suma no definida'
        resta = Vector([])
        for i in range(len(self.vector)):
            resta.vector.append(self.vector[i] - other.vector[i])
        return resta

    def proy(self,other):
        assert type(other) == Vector, 'Proyeccion no definida para escalares' 
        return Vector((self*((self*other)/(self.norma())**2)).vector)

def GSmethod(vectorlst):
    vlst = [Vector([])]*len(vectorlst)
    vhatlst = [Vector([])]*len(vectorlst)
    for i,ui in enumerate(vectorlst):
        if i == 0:
            vlst[0] = ui
        else:
            vlst[i].vector = [0]*len(ui.vector)
            for j in range(i):
                vlst[i] += vhatlst[j].proy(ui)
            vlst[i] = ui - vlst[i]
        vhatlst[i] = vlst[i] * (1 / vlst[i].norma())
    return vhatlst

#PROGRAM
A = Vector([1,0,-1,0])
B = Vector([0,1,1,0])

GS = GSmethod([A,B])
for i in range(len(GS)):
    print(GS[i])
