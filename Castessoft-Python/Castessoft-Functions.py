def sumar_numeros(numero1 = 1, numero2 = 1) -> int: # Esto es una pista de lo que debe retornar la funcion
    return numero1 + numero2

print('Llamado a función con valores por default', sumar_numeros())
print('Llamado a función suma con valores asignados', sumar_numeros(2,10))

#Cuando no se conoce el numero de argumentos
#---------------
# ARGUMENTOS VARIABLES
#---------------
def nombres_estudiantes(*nombres):
    for nombre_individual in nombres:
        print(f'El nombre del estudiante es: {nombre_individual}')

nombres_estudiantes('Juan', 'Carlos', 'Sara', 'Lucas', 'Timoteo')

def sumar_numeros(*args):
    for x in args:
        x *= x
    return x

print('El resultado es {}'.format(sumar_numeros(1,2,3,4,5)))

#----------------
# ENCRIPTAR CON HASHES
#---------------
# ARGUMENTOS VARIABLES LLAVE-VALOR
#---------------
import hashlib

def listar_nombres(**users):
    for key, value in users.items():
        print(f'{key}: {value}')
h=hashlib.new('sha512',b"clavexd")
listar_nombres(juan_castellanos={'Account':'correoexample@examplemail.com','password':h.hexdigest()})

#----------------
# Funciones Recursivas
#---------------- 
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(5)
print(f'El factorial de 5 es {resultado}')


def numeros_desc(numero):
    if numero>0:
        if numero == 1:
            print(1)
        else:
            print(numero)
            numeros_desc(numero-1)
    else: 
        print('No es válido para numeros negativos ')

numeros_desc(5)