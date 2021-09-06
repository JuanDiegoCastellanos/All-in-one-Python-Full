# def print_hi(name):
#     print(f'Hi, {name}')

# if __name__ == '__main__':
#     print_hi('PyCharm')
print("Hello World Python xd")
# Para saber la direccion de memoria de cierta variable se usa el metodo id()
name = "Juan Diego Castellanos"
print(name)
print(id(name))
print("------")
print("tipo de dato")
print(type(name))

# Agregar hints o pistas de que tipo deben ser las variables
last_name: str = "Castellanos Jerez"
print(last_name)

print("---------Day Qualifier--------")
dia = int(input("How was your day? (between 1 to 10 ): "))
print(f"Your day was: {dia}")

print("----------------Book info----------------")
author = input("Please provide the author's name: ")
title = input("Please provide the book's title: ")
print("thanks for your information! ")
print(f"The {title} it was written by {author}")

print("--------------Rectangle Area and Perimeter-------------")
height = int(input("Please provide the height: "))
width = int(input("Please provide the width: "))

print(f"The Area is {(height*width)}")
print(f"The Perimeter is {((height+width)*2)}")



