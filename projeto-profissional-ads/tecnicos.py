import os
import time

from funcoes_coringas import verificar_tel, identificar, gerar_id
from sistema_ordens_de_serviço import mostrar_os

def cadastrar_tecnico(tecnicos : list):
    print("\n" + "=" * 50)
    print("               REGISTRAR TÉCNICO")
    print("=" * 50)
    nome = input("Digite o nome do novo técnico: ").upper().strip()
    tel = verificar_tel()

    if not tel:
        return

    id_tecnico = gerar_id(tecnicos)
    

    tecnicos.append({
        'id' : id_tecnico,
        'nome' : nome,
        'telefone' : tel,
        'os_aberto' : 0,
        'os_finalizada' : 0,
        'historico' : []
    })

def remover_tecnico(tecnicos: list):
    tecnico = identificar(tecnicos)
    if not tecnico:
        return
    tecnicos.remove(tecnico)
    print(f"Técnico '{tecnico['nome']}' removido com sucesso!")
    print("              ORDENS DE SERVIÇO POR TÉCNICOS")
    print("-" * 50)

    for tecnico in tecnicos:
        print(f"NOME: {tecnico['nome']} - - - ORDENS ABERTAS: {tecnico['os_aberto']}")
        print(f"ORDENS FINALIZADAS: {tecnico['os_finalizada']}")

def historico_os (tecnicos : list, finalizadas : list):
    print("\n" + "-" * 50)
    print("              HISTÓRICO DE ORDENS")
    print("-" * 50)

    tecnico = identificar(tecnicos)

    if not tecnico:
        return

    print("=" * 50)
    print("             TÉCNICO ENCONTRADO")
    print(f"                {tecnico['nome']}")
    print("=" * 50)
    if len(tecnico['historico']) == 0:
        print("TÉCNICO NÃO POSSUI ORDENS FINALIZADAS.")
        return
    for id_os in tecnico['historico']:
        for ordem in finalizadas:
            if ordem['id'] == id_os:
                mostrar_os(ordem)
    return

def exibir_tecnicos(tecnicos : list):
    print("\n" + "=" * 50)
    print("       CLIENTES REGISTRADOS")
    print("=" * 50)

    for tecnico in tecnicos:
        print(f"""NOME: {tecnico['nome']} - - - TELEFONE: {tecnico['telefone']}
ORDENS FINALIZADAS: {tecnico['os_finalizada']} - - - ORDENS ABERTAS: {tecnico['os_aberto']} 
-------------------------------------------------------------------------""")

    sair = input("Digite e confirme qualquer tecla pra voltar.")
    time.sleep(0.5)
    os.system('cls')
    return
        
def submenu_tecnicos(tecnicos : list, finalizados : list):
    while True:
        print("\n" + "=" * 50)
        print("                  SETOR TÉCNICOS")
        print("=" * 50)

        print("""[1] - REGISTRAR TÉCNICO - - - [2] - REMOVER TÉCNICO
[3] - HISTÓRICO - - - [4] - EXIBIR TÉCNICOS

[0] VOLTAR """)

        opcao = input('Digite a opção: ')

        match opcao:
            case '1':
                cadastrar_tecnico(tecnicos)
            case '2':
                remover_tecnico(tecnicos)
            case '3':
                historico_os(tecnicos, finalizados)
            case '4':
                exibir_tecnicos(tecnicos)
            case '0':
                time.sleep(0.5)
                os.system('cls')
                return
            case _:
                print("ERROR! Digite uma opção entre 0 e 5.")
    



tecnicos = [
    {
        'id': 1,
        'nome': 'Carlos Henrique',
        'telefone': '74991234567',
        'os_aberto': 0,
        'os_finalizada': 2,
        'historico': [1, 2]
    },
    {
        'id': 2,
        'nome': 'Marcos Oliveira',
        'telefone': '74998765432',
        'os_aberto': 0,
        'os_finalizada': 2,
        'historico': [3, 4]
    }
]


os_finalizadas = [
    {
        'id': 1,
        'cpf_cliente': '11122233344',
        'nome_cliente': 'JOAO SILVA',
        'telefone_cliente': '74991234567',
        'aparelho': 'IPHONE 13',
        'problema': 'Tela quebrada',
        'tecnico': 1,
        'orcamento': {
            'peca_estoque': [
                {
                    'id': 1,
                    'nome': 'Tela iPhone 13',
                    'quantidade': 1,
                    'preco': 450.00
                }
            ],
            'peca_fora': [],
            'fixo': 50.00,
            'total': 500.00
        },
        'status': 'finalizada'
    },

    {
        'id': 2,
        'cpf_cliente': '22233344455',
        'nome_cliente': 'MARIA OLIVEIRA',
        'telefone_cliente': '74992345678',
        'aparelho': 'SAMSUNG GALAXY A54',
        'problema': 'Não liga',
        'tecnico': 1,
        'orcamento': {
            'peca_estoque': [
                {
                    'id': 2,
                    'nome': 'Bateria Galaxy A54',
                    'quantidade': 1,
                    'preco': 180.00
                }
            ],
            'peca_fora': [],
            'fixo': 70.00,
            'total': 250.00
        },
        'status': 'finalizada'
    },

    {
        'id': 3,
        'cpf_cliente': '33344455566',
        'nome_cliente': 'PEDRO SANTOS',
        'telefone_cliente': '74993456789',
        'aparelho': 'MOTOROLA MOTO G84',
        'problema': 'Conector de carga com defeito',
        'tecnico': 2,
        'orcamento': {
            'peca_estoque': [
                {
                    'id': 3,
                    'nome': 'Conector de carga Moto G84',
                    'quantidade': 1,
                    'preco': 90.00
                }
            ],
            'peca_fora': [],
            'fixo': 60.00,
            'total': 150.00
        },
        'status': 'finalizada'
    },

    {
        'id': 4,
        'cpf_cliente': '44455566677',
        'nome_cliente': 'ANA COSTA',
        'telefone_cliente': '74994567890',
        'aparelho': 'NOTEBOOK DELL INSPIRON',
        'problema': 'Superaquecimento',
        'tecnico': 2,
        'orcamento': {
            'peca_estoque': [],
            'peca_fora': [
                {
                    'nome': 'Pasta térmica',
                    'quantidade': 1,
                    'preco': 35.00
                }
            ],
            'fixo': 100.00,
            'total': 135.00
        },
        'status': 'finalizada'
    }
]


