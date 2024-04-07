#ANCHOR - O que é uma classe?
#
#ANCHOR - Quais as vantagens de utilizar uma classe?
#
#ANCHOR - Em uma programação funcional a classe é importante?
#  
#ANCHOR - O que vem a ser paradigma de programação?
#  
#ANCHOR - O pyhton é multiparadigma? Explique
#  
class Carro:
    def __init__(self, nome, marca):
        self._nome = nome
        self._marca = marca

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_marca(self):
        return self._marca

    def set_marca(self, nova_marca):
        self._marca = nova_marca

meu_carro = Carro(nome="Fiesta", marca="Ford")

print(f"Nome do carro: {meu_carro.get_nome()}")
print(f"Marca do carro: {meu_carro.get_marca()}")

meu_carro.set_nome("Focus")
meu_carro.set_marca("Ford")

print(f"Nome do carro atualizado: {meu_carro.get_nome()}")
print(f"Marca do carro atualizada: {meu_carro.get_marca()}")
