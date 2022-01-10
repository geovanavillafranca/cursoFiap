class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.soma())
print(calculadora.divisao())
print(calculadora.multiplicacao())
print(calculadora.subtracao())



# aqui passa todo os valores quando for chamado
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self, valor_a, valor_b):
        return self.valor_a + self.valor_b

    def subtracao(self, valor_a, valor_b):
        return self.valor_a - self.valor_b

    def multiplicacao(self, valor_a, valor_b):
        return self.valor_a * self.valor_b

    def divisao(self, valor_a, valor_b):
        return self.valor_a / self.valor_b


calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.soma(3, 2))
print(calculadora.divisao(4, 5))
print(calculadora.multiplicacao(5, 2))
print(calculadora.subtracao(6, 3))





