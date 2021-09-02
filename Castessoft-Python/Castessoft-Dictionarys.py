terminos = {'OOP': 'Object Oriented Programming',
            'IDE': 'Integrated Development Enviroment', 
            'DBMS': 'DataBase Management System'}

print(f"Element for key OOP => {terminos['OOP']}")
print('OOP', terminos.get('OOP'))
#Modificar por key
terminos['OOP'] = 'Ooo setenta'
print(terminos.get('OOP'))

for llave, valor in terminos.items(): # para solo llaves .keys() o solo valores .values()
    print(llave, valor)