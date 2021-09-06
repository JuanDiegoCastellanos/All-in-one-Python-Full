# class Persona:
#     #def __init__(self):
#     def __init__(self,nombre,apellido,edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad

# persona1 = Persona('Juan','Castellanos',21)
# print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# #Modificar atributos directamente
# persona1.nombre = 'Juan Manuel'
# persona1.apellido = 'Juarez'
# persona1.edad = 34
# print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')


# persona2 = Persona('Gabriela','Rodriguez', 20)
# print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

class Person:
    # self puede llamarse this, pero en python se recomienda el uso de self
    def __init__(self, name:str, last_name:str, age:int):
        self.name = name
        self.last_name = last_name
        self.age = age
    def show_details(self):
        print(f'Person: {self.name} {self.last_name} {self.age}')
    
persona1 = Person('Juan', 'Castellanos',21)
persona1.show_details()

print('-------------')
#Otra forma de llamar metodos, pero requieren por parametro un objeto
Person.show_details(persona1)
persona1.telefono = '3223432343'
print(f'Telefono de persona1 :{persona1.telefono}')



persona2 = Person('Gabriela', 'Rodriguez', 20)
persona2.show_details()
