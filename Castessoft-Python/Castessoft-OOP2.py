# class Person:
#     """
#     - Tema: clase persona con metodo inicializador con argumentos, variables, de tipo tupla y diccionario
#     - Atributos: nombre, edad, apellido, (numero_telefonico, dirección, peso, altura), {correo:correo, profesion:profesion}
#     """
#     def __init__(self, name, last_name, age, *details0,**details1):
#         #details indica que ingresa un argumento variable de tipo TUPLA
#         #details1 indica que ingresa un argumento variable de tipo DICCIONARIO
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.details0 = details0
#         self.details1 = details1
#     def show_details(self):
#         return f'\nNombre: {self.name}\nApellido: {self.last_name}\nEdad: {self.age}\nDetalles1: {self.details0}\nDetalles2: {self.details1}'

# person0 = Person('Juan','Castellanos',21,3223067599,'calle 10-No 10-74',62.5,1.72, correo='juan.castellanosj@usantoto.edu.co',profesion='Ingenieria de Sistemas')
# print(f'Los detalles de la persona son: {person0.show_details()}')

class Person:

    def __init__(self, name, last_name, age):
        '''
        self.name = name #Atributo Público
        self._name = name #Atributo Encapsulado
        self.__name = name #Atributo Restringido a Encapsulación        
        '''
        self._name = name 
        self._last_name = last_name
        self._age = age
    
    '''
    Decorador property indica que el metodo devuelve el valor del atributo
    '''
    @property 
    def get_name(self):
        print('Llamando método get name')
        return self._name
    '''
    Decorador nombre_atributo.setter indica que el metodo va cambiar el valor del atributo
    Para definir cual es el setter del atributo se hace llamado al metodo getter de dicho atributo
    
    Se recomienda usar el mismo nombre de los atributos
    '''
    @get_name.setter 
    def set_name(self, name):
        print('Llamado el setter de nombre')
        self._name = name   

    #-----------------------------------
    @property 
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def show_details(self):
        return f'\nName: {self._name}\nLast Name: {self._last_name}\nAge: {self._age}\n'

person0 = Person('Juan', 'Castellanos',21)

'''
person0._name= 'Diego'
Se puede modificar el nombre sin embargo el carácter underscore sugiere que ese atributo
solo se pueda modificar desde la instacia de la clase (Objeto)
'''
print(f'Name:{person0.get_name}')
print(person0.show_details())

print(f'Name: {person0.get_name}')

person0.set_name = 'Juan Diego' 
# Se Settea como si fuera un atributo pero en realidad hace llamado al metodo set_name, ya que se le indico
# su función con el decorador y el nombre del metodo get para hacer referencia al atributo encapsulado
print(f'New Name: {person0.get_name}')
# Se trae el valor del atributo por medio del metodo como si fuera un atributo, 
# se hace la llamada indirectamente al metodo

person0.age = 34
print(f'Age: {person0.age}')

person0.last_name = 'Rodriguez'
print(f'Last name: {person0.last_name}')
