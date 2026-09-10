from sistema_clientes import registrarClientes, RegistrarEquipamentos, exibir_cliente, pesquisar_cliente, excluir_cliente, menu_clientes, adicionar_historico 
from sistema_ordens_de_serviço import abrir_OSs, mostrar_os, orcamento_Os, aprovar_Os, finalizar_Os
from sistema_estoque_add import gerenciar_estoque_manual, cadastrar_peca, listar_pecas, pesquisar_peca, remover_peca, menu_estoque
from submenu_os import submenu_ordens
from tecnicos import submenu_tecnicos

from collections import deque
import os
from funcoes_coringas import verificar_cpf

### FILAS DO SISTEMA ###
fila_orcamento = deque()
fila_aprovacao = deque()
fila_execucao = deque()
finalizados = []

### LISTAS DE DICTS DO SISTEMA ###
estoque = [
    {
        'id' : 1,
        'nome' : "BATERIA SAMSUNG",
        'categoria' : "BATERIA",
        'quantidade' : 14,
        'estado' : "novo",
        'preco' : 10.50
        },
    {
        'id' : 2,
        'nome' : "TELA SAMSUNG A32",
        'categoria' : 'TELA',
        'quantidade' : 3,
        'estado' : 'usado',
        'preco' : 280.00
        },
    {
        'id' : 3,
        'nome' : "TELA REDMI NOTE 10",
        'categoria' : "TELA",
        'quantidade' : 2,
        'estado' : 'novo',
        'preco' : 150.00
    },

    {
        'id' : 4,
        'nome' : "CONECTOR CARGA MOTO G8",
        'categoria' : "CONECTOR",
        'quantidade' : 15,
        'estado' : "novo",
        'preco' : 12.00
    },
    {
         'id' : 5,
         'nome' : "CAMERA TRASEIRA IPHONE XR",
         'categoria' : "CAMERA",
         'quantidade' : 8,
         'estado' : "novo",
         'preco' : 350.00,     
    },
    {
         'id' : 6,
         'nome' : "TAMPA TRASEIRA DE VIDRO IPHONE 11",
         'categoria' : "CARCAÇA",
         'quantidade' : 5,
         'estado' : "novo",
         'preco' : 90.00,     
     },
    {
         'id' : 7,
         'nome' : "FLEX BOTAO POWER E VOLUME A20",
         'categoria' : "FLEX",
         'quantidade' : 20,
         'estado' : "usado",
         'preco' : 15.00,     
     },
    {
         'id' : 8,
         'nome' : "BATERIA IPHONE 11",
         'categoria' : "BATERIA",
         'quantidade' : 9,
         'estado' : "novo",
         'preco' : 135.00,     
     },    
]

clientes = [
    {
    "nome" : "Alanzoka Silva Batista",
    "cpf" : "11122233344",
    "telefone": "74888899999",
    "historico": []
},
{
    "nome" : "TazerCraft Junior",
    "cpf" : "22233344455",
    "telefone": "74888889999",
    "historico": []
}
]

tecnicos = [{
    'id' : 2,
    'nome' : "Orretadinha",
    'telefone' : '4002-8922',
    'os_aberto' : 0,
    'os_finalizada' : 0,
    'historico' : []
},
{   
    'id' : 1,
    'nome' : "Olokinho",
    'telefone' : '4002-8922',
    'os_aberto' : 0,
    'os_finalizada' : 0,
    'historico' : []
}]

### MENU PRINCIPAL ###
proximo_id = 1

def main():
    while True:
        print("\n" + "=" * 50)
        print("       SISTEMA PARA ASSISTÊNCIA TÉCNINCA")
        print("=" * 50)

        print("""[1] - SETOR CLIENTES - - - [2] - ESTOQUE 
[3] - ORDENS DE SERVIÇOS - - - [4] - TÉCNICOS

[0] FECHAR """)
        opcao = input("Digite o número conforme as opções acima: ")

        match opcao:
            case '1':
                menu_clientes(clientes)
            case '2':
                menu_estoque(estoque)
            case '3':
                submenu_ordens(fila_orcamento, fila_aprovacao, fila_execucao, finalizados, tecnicos, clientes, estoque, proximo_id)
            case '4':
                submenu_tecnicos(tecnicos, finalizados)
            case '0':
                break
            case _:
                print("ERROR! Digite um número de 0 e 3.")

if __name__ == "__main__":
    main()