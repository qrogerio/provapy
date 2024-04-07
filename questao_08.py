from questao_07 import Carro

meu_carro = Carro(nome="Fiesta", marca="Ford")

print(f"Nome do carro: {meu_carro.get_nome()}")
print(f"Marca do carro: {meu_carro.get_marca()}")

meu_carro.set_nome("Focus")
meu_carro.set_marca("Ford")

print(f"Nome do carro atualizado: {meu_carro.get_nome()}")
print(f"Marca do carro atualizada: {meu_carro.get_marca()}")