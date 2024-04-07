#lista das compras
lista_compras = ["arroz", "feijão", "quiabo"]

# 1. pop: Remove o último elemento da lista e retorna o valor removido
ultimo_item = lista_compras.pop()
print(f"Último item removido: {ultimo_item}")
print(f"Lista atualizada: {lista_compras}")

# 2. index: Retorna o índice do primeiro elemento com o valor especificado
indice_feijao = lista_compras.index("feijão")
print(f"Índice do feijão: {indice_feijao}")

# 3. count: Conta quantas vezes um elemento aparece na lista
quantidade_arroz = lista_compras.count("arroz")
print(f"Quantidade de arroz: {quantidade_arroz}")

# 4. sort: Ordena a lista em ordem alfabética (ou numérica)
lista_compras.sort()
print(f"Lista ordenada: {lista_compras}")

# 5. reverse: Inverte a ordem dos elementos na lista
lista_compras.reverse()
print(f"Lista invertida: {lista_compras}")
