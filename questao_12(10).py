import flet as ft 
def main(page: ft.Page):
    interacoes = ""

    lista_demo = ["Java", "Python", "C#"]
    for linguagem in lista_demo:
        interacoes += str(linguagem) + ","
    
    interacoes = interacoes[:-2]
    text_interacoes = ft.Text(value=interacoes)
    page.controls.append(text_interacoes)
    page.update()

ft.app(main)





