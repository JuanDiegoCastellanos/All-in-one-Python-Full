class Aritmetica:
    def __init__(self, operandoA, operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB

    def suma(self):
        return self.operandoA + self.operandoB
    def resta(self):
        return self.operandoA - self.operandoB
    def multiplicacion(self):
        return self.operandoA * self.operandoB
    def divicion(self):
        return self.operandoA / self.operandoB 

    
aritmetica = Aritmetica(12, 2)

print(f'La suma es: {aritmetica.suma()}')
print(f'La resta es: {aritmetica.resta()}')
print(f'La multiplicacion es: {aritmetica.multiplicacion()}')
print(f'La divicion es: {aritmetica.divicion():.2f}')
