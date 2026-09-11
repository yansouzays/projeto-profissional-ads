import os
import time
from funcoes_coringas import gerar_id

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

def gerenciar_estoque_manual(estoque : list):

    print("\n ---- GERENCIAMENTO DE ESTOQUE ----")

    try:
        id_peca = int(input("INFORME O ID DA PEÇA: "))
    except ValueError:
        print ("ERRO: o ID deve ser um numero inteiro!")
        return

    peca_encontrada = None
    for item in estoque:
        if item['id'] == id_peca:
            peca_encontrada = item
            break

    if peca_encontrada is None:
        print ("ERRO: peça não encontrada no estoque!")
        return

    print(f"PEÇA SELECIONADA: {peca_encontrada['nome']}")
    print(f"QUANTIDADE EM ESTOQUE:{peca_encontrada['quantidade']}")

    operacao = input("Deseja (A)dicionar ou (R)emover peças?").strip().upper()

    if operacao not in [ 'A', 'R']:
        print("OPÇÃO INVÁLIDA!")
        return

    try:
        quantidade = int(input("INFORME A QUANTIDADE: "))
        if quantidade <= 0:
            print("ERROR! A quantidadde deve ser maior que zero!")
            return
    except ValueError:
        print("ENTRADA INVÁLIDA! Digite apenas numeros inteiros.")
        return

    if operacao == 'A':
        peca_encontrada['quantidade'] += quantidade
        print(f"ADICIONADAS {quantidade} UNIDADES. NOVO SALDO DE '{peca_encontrada['nome']}': {peca_encontrada['quantidade']}")
    elif operacao =='R':
        if quantidade > peca_encontrada['quantidade']:
            print (f"Erro: Saldo insuficiente em estoque! Saldo atual: {peca_encontrada['quantidade']}")
            time.sleep(1)
            os.system('cls')
            return
        peca_encontrada['quantidade']-= quantidade
        print(f"REMOVIDAS{quantidade} UNIDADES. NOVO SALDO DE '{peca_encontrada['nome']}' : {peca_encontrada['quantidade']}")
        time.sleep(1)
        os.system('cls')

def cadastrar_peca(estoque: list):
    print("\n" + "=" * 50)
    print("               CADASTRAR PEÇA")
    print("=" * 50)

    id_peca = gerar_id(estoque)
    
    for item in estoque:
        if item['id'] == id_peca:
            print("Erro: já existe uma peça com esse ID!")
            return

    nome = input("INFORME O NOME DA PEÇA: ").strip().upper()
    categoria = input("INFORME A CATEGORIA (ex: BATERIA, FLEX, TELA): "). strip().upper()
    estado = input("INFORME O ESTADO (NOVO/USADO): ").strip().upper()

    try:
        quantidade = int(input("INFORME A QUANTIDADE INICIAL: "))
        preco = float(input("INFORME O PREÇO (R$): "))
    except ValueError: 
        print("Erro: Digite valores válidos para quantidade e preço" )
        return

    nova_peca = {
        'id': id_peca,
        'nome':nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'estado': estado,
        'preco': preco
    }

    estoque.append(nova_peca)
    print (f"PEÇA '{nome}' CADASTRADA COM SUCESSO!")
    time.sleep(1)
    os.system('cls')

def listar_pecas(estoque: list):

    print("\n ------- LISTA DE PEÇAS / EQUIPAMENTOS -------")
    if not estoque:
        print("Nenhuma peça cadastrada.")
        return
    print(f"{'ID':<5} | {"Nome":<30} | {'Categoria' :<12} | {'estado' :<8} | {'Quandidade':<6} | {'Preço(R$)':<10}")
    print("-" * 80)
    for item in estoque:
        print(f"{item['id']:<5}) | {item['nome']:<30} | {item['categoria']:<12} | {item['estado']:<8} | {item['quantidade']:<6} | R$ {item['preco']:<9.2f}")
    sair = input("APERTE ENTER PARA SAIR: ")
    time.sleep(1)
    os.system('cls')
    return

def pesquisar_peca(estoque:list):
    print("\n" + "=" * 50)
    print("               PESQUISAR PEÇA")
    print("=" * 50)
    termo = input("Informe o ID ou nome para buscar: ").strip().upper()

    encontradas = []
    for item in estoque:
        if termo == str(item['id']) or termo in item['nome'].upper():
            encontradas.append(item)

    if encontradas:
        print(f"\nResultado(s) encontrado(s):")
        print(f"{'ID':<5} | {'Nome':<30} | {'Categoria' :<12} | {'estado' :<8} | {'Quandidade':<6} | {'Preço(R$)':<10}")
        print ("-" * 80)
        for item in encontradas:
            print(f"{item['id']:<5}) | {item['nome']:<30} | {item['categoria']:<12} | {item['estado']:<8} | {item['quantidade']:<6} | R$ {item['preco']:<9.2f}")

        sair = input("APERTE ENTER PARA VOLTAR: ")
        time.sleep(1)
        os.system('cls')
        return

    else:
        print("Nenhuma peça encontrada com esse termo.")
        time.sleep(1)
        os.system('cls')


def remover_peca(estoque: list):

    print("\n" + "=" * 50)
    print("               REMOVER PEÇA")
    print("=" * 50)

    print("DIGITE [0] E CONFIME PARA VOLTAR")
    try:
        id_peca = int(input("INFORME O ID DA PEÇA A SER REMOVIDO: "))
    except ValueError:
        print("Erro: O ID deve ser um numero inteiro!")
        return

    if id_peca == 0:
        return

    for item in estoque:
        if item['id'] == id_peca:
            estoque.remove(item)
            print(f" '{item['id']}' (ID: {id_peca}) REMOVIDA DO CADASTRO COM SUCESSO!")
            time.sleep(1)
            os.system('cls')
            return

    print("ERROR! Peça não encontrada no estoque.")

def menu_estoque(estoque):
    while True:
        print("\n" + "="*40)
        print("   GERENCIAMENTO DE PEÇAS / EQUIPAMENTOS")
        print("="*40)

        print("""[1] CADASTRAR PEÇA - - - [2] LISTAR PEÇAS
[3] PESQUISAR PEÇA - - - [4] REMOVER PEÇA
[5] ALTERAR ESTOQUE

[0] VOLTAR""")

        opcao = input("\nEscolha uma opção: ").strip()

        match opcao:
            case '1':
                cadastrar_peca(estoque)
            case '2':
                listar_pecas(estoque)
            case '3':
                pesquisar_peca(estoque)
            case '4':
                remover_peca(estoque)
            case '5':
                gerenciar_estoque_manual(estoque)
            case '0':
                os.system('cls')
                return
            case _:
                print("ERROR! Digite um número entre 0 e 5.")

if __name__ == "__main__":
    menu_estoque()