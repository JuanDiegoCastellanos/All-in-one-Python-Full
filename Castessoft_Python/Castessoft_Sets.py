# Set o Conjuntos
credentials = ['correo@dominio.com', 'clave1234567']
conjunto = set(credentials)
print(conjunto)
# El set o conjunto solo permite AGREGAR O ELIMINAR, NO REPETIDOS y NO MANTIENE UN ORDEN
conjunto.add(True)  # Por ejemplo true para saber si tiene licencia
print(conjunto)
set_frutas = {"fresa", "piña", "cereza"}
set_frutas.update(["sandía", "melón", "mango"])
print(set_frutas)
