import flet as ft   

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def get_nome(self):
        return self.nome

    def get_marca(self):
        return self.marca

def main(page: ft.Page):
    carro = Carro(nome="Fusca", marca="Volkswagen")
    
    nome_carro = ft.TextField(value=carro.get_nome(), disabled=True)
    marca_carro = ft.TextField(value=carro.get_marca(), disabled=True)
    
    page.add(ft.Text("Nome do carro:"), nome_carro)
    page.add(ft.Text("Marca do carro:"), marca_carro)

ft.app(target=main)