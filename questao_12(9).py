import flet as ft 
def main(page: ft.Page):
    # Inicializa uma string vazia para armazenar as iterações
    iteracoes = ""
    
    tupla_demo = ("Eu","Tu","Ele")
    for elemento in tupla_demo:
        # Adiciona o nome atual e uma vírgula à string
        iteracoes += str(elemento) + ", "
    
    # Remove a última vírgula e espaço da string
    iteracoes = iteracoes[:-2]
    
    # Cria um controle de texto para exibir as iterações
    texto_iteracoes = ft.Text(value=iteracoes)
    
    # Adiciona o controle de texto à página e atualiza
    page.controls.append(texto_iteracoes)

    '''A tupla não pode ser alterada sendo uma tupla
        mas pode ser alterada, transformando-a em lista.
    '''
    page.update() 
ft.app(target=main)