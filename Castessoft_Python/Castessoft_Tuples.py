#Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
# navegación inversa
print("Inverso->",frutas[-1])
# acceder a un rango
print(frutas[0:1])# sin incluir el último índice


tupla = ('Castellanos', 'Juan', 'Diego')

for i in tupla:
    print(i, end='------')

tuplaLista = list(tupla)
tuplaLista[0]= 221212
tupla = tuple(tuplaLista)


print(f'\n This updated tuple is {tupla}')

del tupla