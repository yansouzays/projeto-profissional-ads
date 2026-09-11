from sistema_clientes import menu_clientes
from sistema_ordens_de_serviço import abrir_OSs, mostrar_os, orcamento_Os, aprovar_Os, finalizar_Os
from sistema_estoque_add import menu_estoque
from submenu_os import submenu_ordens
from tecnicos import submenu_tecnicos

from collections import deque
import os
from funcoes_coringas import verificar_cpf

### FILAS DO SISTEMA ###
fila_orcamento = deque([{
        'id': 5,
        'cpf_cliente': '99988877766',
        'nome_cliente': 'PEDRO ALMEIDA',
        'telefone_cliente': '11977773333',
        'aparelho': 'XIAOMI REDMI NOTE 10',
        'problema': 'NAO CARREGA',
        'tecnico': None,
        'orcamento': {
            'peca_estoque': [],
            'peca_fora': [],
            'fixo': 0,
            'total': 0
        },
        'status': 'ORCAMENTO'
    }])
fila_aprovacao = deque([
        {
        'id': 4,
        'cpf_cliente': '44433322211',
        'nome_cliente': 'LUCAS LIMA',
        'telefone_cliente': '11966664444',
        'aparelho': 'SAMSUNG A32',
        'problema': 'TELA QUEBRADA',
        'tecnico': None,
        'orcamento': {
            'peca_estoque': [
                {
                    'id': 2,
                    'nome': 'TELA SAMSUNG A32',
                    'preco': 280.00,
                    'quantidade': 1
                }
            ],
            'peca_fora': [],
            'fixo': 100.00,
            'total': 380.00
        },
        'status': 'APROVACAO'
        }
    ]
)
fila_execucao = deque([
    {
        'id': 3,
        'cpf_cliente': '99988877766',
        'nome_cliente': 'PEDRO ALMEIDA',
        'telefone_cliente': '11977773333',
        'aparelho': 'MOTO G8',
        'problema': 'CONECTOR DANIFICADO',
        'tecnico': 'ANA SOUZA',
        'orcamento': {
            'peca_estoque': [
                {
                    'id': 4,
                    'nome': 'CONECTOR CARGA MOTO G8',
                    'preco': 12.00,
                    'quantidade': 1
                }
            ],
            'peca_fora': [],
            'fixo': 80.00,
            'total': 92.00
        },
        'status': 'EXECUCAO'
    }
])
finalizados = [{
        'id': 1,
        'cpf_cliente': '11122233344',
        'nome_cliente': 'JOAO PEREIRA',
        'telefone_cliente': '11999991111',
        'aparelho': 'IPHONE 11',
        'problema': 'BATERIA VICIADA',
        'tecnico': 'CARLOS SILVA',
        'orcamento': {
            'peca_estoque': [
                {
                    'id': 8,
                    'nome': 'BATERIA IPHONE 11',
                    'preco': 135.00,
                    'quantidade': 1
                }
            ],
            'peca_fora': [],
            'fixo': 100.00,
            'total': 235.00
        },
        'status': 'FINALIZADO'
    },
    {
        'id': 2,
        'cpf_cliente': '55566677788',
        'nome_cliente': 'MARIA SANTOS',
        'telefone_cliente': '11988882222',
        'aparelho': 'IPHONE XR',
        'problema': 'CAMERA TRASEIRA QUEBRADA',
        'tecnico': None,
        'orcamento': {
            'peca_estoque': [
                {
                    'id': 5,
                    'nome': 'CAMERA TRASEIRA IPHONE XR',
                    'preco': 350.00,
                    'quantidade': 1
                }
            ],
            'peca_fora': [],
            'fixo': 150.00,
            'total': 500.00
        },
        'status': 'CANCELADO'
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
        "nome": "JOAO PEREIRA",
        "telefone": "11999991111",
        "cpf": "11122233344",
        "historico": [1]  # ID DA OS 1 (FINALIZADA)
    },
    {
        "nome": "MARIA SANTOS",
        "telefone": "11988882222",
        "cpf": "55566677788",
        "historico": [2]  # ID DA OS 2 (CANCELADA)
    },
    {
        "nome": "PEDRO ALMEIDA",
        "telefone": "11977773333",
        "cpf": "99988877766",
        "historico": []   # NENHUMA OS FINALIZADA
    },
    {
        "nome": "LUCAS LIMA",
        "telefone": "11966664444",
        "cpf": "44433322211",
        "historico": []   # NENHUMA OS FINALIZADA
    }
]

tecnicos = [
    {
        "id": 1,
        "nome": "CARLOS SILVA",
        "telefone": "11911110000",
        "os_aberto": 0,
        "os_finalizada": 1,
        "historico": [1] 
    },
    {
        "id": 2,
        "nome": "ANA SOUZA",
        "telefone": "11922220000",
        "os_aberto": 1,
        "os_finalizada": 0,
        "historico": []
    }
]

### MENU PRINCIPAL ###
proximo_id = 6

def main():
    while True:
        print("\n" + "=" * 50)
        print("       SISTEMA PARA ASSISTÊNCIA TÉCNINCA")
        print("=" * 50)

        print("""[1] - SETOR CLIENTES - - - [2] - ESTOQUE 
[3] - ORDENS DE SERVIÇOS - [4] - TÉCNICOS

[0] FECHAR """)
        opcao = input("Digite o número conforme as opções acima: ")

        match opcao:
            case '1':
                menu_clientes(clientes, finalizados)
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