class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def __add__(self,other):
        return Vector(self.x + other.x ,self.y + other.y ,self.z + other.z)

    def suma(self,other):
        
a = Vector(1,2,3)
b = Vector(4,6,5)
print(a+b)