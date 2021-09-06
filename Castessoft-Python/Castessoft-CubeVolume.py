class Cube:
    def __init__(self, width=0, height=0, deep=0):
        self.width = width
        self.height = height
        self.deep = deep

    def volume(self):
        return self.width * self.height * self.deep
    
cube = Cube(int(input('Digite el ancho \n ---> ')), int(input('Digite la profundidad \n --> ')), int(input('Digite la altura \n --> ')))
print(f'El volumen del cubo es: {cube.volume()} m')