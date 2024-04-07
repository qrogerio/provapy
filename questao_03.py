nome_maquina = input("Digite o nome da máquina: ")
tempo_uso = int(input("Digite o tempo de uso da máquina: "))
ligado = bool(input("A máquina está ligada? (Sim/Não): "))

print(f"Nome da máquina: {nome_maquina}")
print(f"Tempo de uso da máquina: {tempo_uso}")
print(f"Máquina está ligada? {ligado}")

print(f"Tipo de nome_maquina: {type(nome_maquina)}")
print(f"Tipo de tempo_uso: {type(tempo_uso)}")
print(f"Tipo de ligado: {type(ligado)}")
