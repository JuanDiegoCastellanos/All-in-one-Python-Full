class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base*self.height

rectangle = Rectangle(int(input('Proporciona la base \n --> ')),int(input('Proporciona la altura \n ---> ')))
print(f'El area del rectangulo es : {rectangle.area()}')