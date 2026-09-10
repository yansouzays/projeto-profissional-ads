from sistema_clientes import registrarClientes, RegistrarEquipamentos, exibir_cliente, pesquisar_cliente, excluir_cliente, menu_clientes, adicionar_historico 
from sistema_ordens_de_serviço import abrir_OSs, mostrar_os, orcamento_Os, aprovar_Os, finalizar_Os
from sistema_estoque_add import gerenciar_estoque_manual, cadastrar_peca, listar_pecas, pesquisar_peca, remover_peca, menu_estoque
from submenu_os import submenu_ordens
from tecnicos import submenu_tecnicos

from collections import deque
import os
from funcoes_coringas import verificar_cpf

### FILAS DO SISTEMA ###
fila_orcamento = deque([{
    "id": 5,
    "cpf_cliente": "11122233344",
    "nome_cliente": "JOAO DA SILVA",
    "telefone_cliente": "74999990001",
    "aparelho": "IPHONE 11",
    "problema": "TELA QUEBRADA",
    "tecnico": "PEDRO ALMEIDA",
    "orcamento": {
        "peca_estoque": [],
        "peca_fora": [],
        "fixo": 0,
        "total": 0
    },
    "status": "ORCAMENTO"
}])
fila_aprovacao = deque([
    {
        "id": 4,
        "cpf_cliente": "22233344455",
        "nome_cliente": "MARIA OLIVEIRA",
        "telefone_cliente": "74999990002",
        "aparelho": "SAMSUNG GALAXY A54",
        "problema": "NAO LIGA",
        "tecnico": "LUCAS MENDES",
        "orcamento": {
            "peca_estoque": [
                {
                    "id": 1,
                    "nome": "BATERIA GALAXY A54",
                    "quantidade": 1,
                    "preco": 180
                }
            ],
            "peca_fora": [],
            "fixo": 50,
            "total": 230
        },
        "status": "APROVACAO"
    }
])
fila_execucao = deque([
    {
        "id": 3,
        "cpf_cliente": "33344455566",
        "nome_cliente": "CARLOS SANTOS",
        "telefone_cliente": "74999990003",
        "aparelho": "NOTEBOOK DELL INSPIRON",
        "problema": "NAO INICIA O WINDOWS",
        "tecnico": "PEDRO ALMEIDA",
        "orcamento": {
            "peca_estoque": [],
            "peca_fora": [],
            "fixo": 120,
            "total": 120
        },
        "status": "EXECUCAO"
    }
])
finalizados = [{
        "id": 1,
        "cpf_cliente": "11122233344",
        "nome_cliente": "JOAO DA SILVA",
        "telefone_cliente": "74999990001",
        "aparelho": "MOTOROLA G84",
        "problema": "CONECTOR DE CARGA DANIFICADO",
        "tecnico": "PEDRO ALMEIDA",
        "orcamento": {
            "peca_estoque": [
                {
                    "id": 2,
                    "nome": "CONECTOR DE CARGA MOTOROLA G84",
                    "quantidade": 1,
                    "preco": 90
                }
            ],
            "peca_fora": [],
            "fixo": 60,
            "total": 150
        },
        "status": "FINALIZADA"
    },
    {
        "id": 2,
        "cpf_cliente": "33344455566",
        "nome_cliente": "CARLOS SANTOS",
        "telefone_cliente": "74999990003",
        "aparelho": "PLAYSTATION 4",
        "problema": "SUPERAQUECIMENTO",
        "tecnico": "LUCAS MENDES",
        "orcamento": {
            "peca_estoque": [],
            "peca_fora": [
                {
                    "nome": "PASTA TERMICA",
                    "quantidade": 1,
                    "preco": 45
                }
            ],
            "fixo": 100,
            "total": 145
        },
        "status": "FINALIZADA"
    }]

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
        "nome": "JOAO DA SILVA",
        "telefone": "74999990001",
        "cpf": "11122233344",
        "historico": [1, 4]
    },
    {
        "nome": "MARIA OLIVEIRA",
        "telefone": "74999990002",
        "cpf": "22233344455",
        "historico": [2]
    },
    {
        "nome": "CARLOS SANTOS",
        "telefone": "74999990003",
        "cpf": "33344455566",
        "historico": [3, 5]
    },
    {
        "nome": "ANA SOUZA",
        "telefone": "74999990004",
        "cpf": "44455566677",
        "historico": []
    }
]

tecnicos = [{
        "id": 1,
        "nome": "PEDRO ALMEIDA",
        "telefone": "74988880001",
        "os_aberto": 1,
        "os_finalizada": 2,
        "historico": [1, 3, 4]
    },
    {
        "id": 2,
        "nome": "LUCAS MENDES",
        "telefone": "74988880002",
        "os_aberto": 1,
        "os_finalizada": 1,
        "historico": [2, 5]
    }]

### MENU PRINCIPAL ###
proximo_id = 6

def main():
    while True:
        print("\n" + "=" * 50)
        print("       SISTEMA PARA ASSISTÊNCIA TÉCNINCA")
        print("=" * 50)

        print("""[1] - SETOR CLIENTES - - - [2] - ESTOQUE 
[3] - ORDENS DE SERVIÇOS   - - -  [4] - TÉCNICOS

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