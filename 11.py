lista_compras = ["arroz", "feijão", "quiabo"]

ultimo_item = lista_compras.pop()
print("Último item removido: " + ultimo_item)
print("Lista atualizada: " + str(lista_compras))

indice_feijao = lista_compras.index("feijão")
print("Índice do feijão: " + str(indice_feijao))

quantidade_arroz = lista_compras.count("arroz")
print("Quantidade de arroz: " + str(quantidade_arroz))

lista_compras.sort()
print("Lista ordenada: " + str(lista_compras))

lista_compras.reverse()
print("Lista invertida: " + str(lista_compras))
