import flet as ft  
from questao_07 import Carro

def main(page: ft.Page):
    carro = Carro(nome="Fusca", marca="Volkswagen")
    
    nome_carro = ft.TextField(value=carro.get_nome(), disabled=True)
    marca_carro = ft.TextField(value=carro.get_marca(), disabled=True)
    
    page.add(ft.Text("Nome do carro:"), nome_carro)
    page.add(ft.Text("Marca do carro:"), marca_carro)

ft.app(target=main)
