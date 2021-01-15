class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def area(self):
        return (self.lado)**2

class Cuadrado1(Cuadrado):
    def __init__(self,lado):
        super().__init__(lado)

    def perimetro(self):
        return 4 * self.lado

##Main

def main():
    a = input('Ingrese lado del cuadrado: ')
    cuadrado = Cuadrado1(int(a))
    print(f'\tEl área del cuadrado es: {cuadrado.area()}\
    \n\tEl perímetro del cuadrado es: {cuadrado.perimetro()}')
main()