#----------------------
# LOOP-FOR EXAMPLES 
#----------------------

for word in "Juan Diego Castellanos":
    if word == "l":
        print(f" Found {word}")

#----------------------
# LOOP-FOR WITH RANGE
#----------------------
for i in range(6):
    if i % 2 == 0:
        print(f"Value :{i}")
for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Value : {i}")

for i in range(10):
    if i % 3 == 0:
        print(f"El numero {i} es divisible en 3", end="\n")

#--------------------
# LOOP-WHILE EXAMPLE
#--------------------
condicion = True

while condicion:
    print('Ejecutando ciclo while')
else:
    print('Fin del ciclo while')

contador = 0
while contador < 3:
    print(contador)
    contador += 1 #contador = contador + 1
else:
    print('Fin ciclo while')


#--------------------
# WORD BREAK
#-------------------
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for')

#---------------------
# WORD CONTINUE
#---------------------
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')