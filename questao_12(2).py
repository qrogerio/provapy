'''nome = input("Digite o seu nome: ")
nome_maiusculo = nome.upper()#.lower para deixar em letras maiusculas
print(f"Seu nome em letras minúsculas: {nome_maiusculo}")'''
import flet as ft

def main(Page:ft.Page):
    mensagem = ft.Text("Converter nome para letras maiúsculas")
    nome = ft.TextField(label="Digite seu nome: ")

    def btn_click(e):
        nome_maiusculo = ft.Text(nome.value.upper())
        nome.value = ""
        Page.add(nome_maiusculo)
        Page.update()
    btn = ft.ElevatedButton("Converter para maiúsculo", on_click=btn_click)
    Page.update()
    Page.add(mensagem,nome,btn)
        

ft.app(main)