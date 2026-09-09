import os
from funcoes_coringas import verificar_cpf, verificar_tel


def registrarClientes(clientes: list):
    print("\n" + "=" * 50)
    print("       CADASTRAR CLIENTES")
    print("=" * 50)

    nome = input("Digite o nome do cliente: ").upper().strip()

    cpf = verificar_cpf()
    if not cpf:
        return

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("\nErro. Já existe um cliente cadastrado com este CPF!\nTente novamente.")
            return
        
    telefone = verificar_tel()
    if not telefone:
        return

    for cliente in clientes:
            if cliente["telefone"] == telefone:
                print("\nErro. Já existe um cliente cadastrado com este telefone!\nTente novamente.")
                return
    
    client = {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf
    }
    clientes.append(client)
    print("\nCliente cadastrado com sucesso!")

def exibir_cliente(clientes):
    print("\n" + "=" * 50)
    print("       CLIENTES CADASTRADOS")
    print("=" * 50)

    if not clientes:
        print("Nenhum cliente cadastrado até o momento!")
    else:
        print("\n--- LISTA DE CLIENTES ---")
        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"CPF: {cliente['cpf']}")
            print("-" * 25)

def pesquisar_cliente(clientes):
    print("\n" + "=" * 50)
    print("       PESQUISAR CLIENTES")
    print("=" * 50)

    cpf_cliente = verificar_cpf()
    if not cpf_cliente:
        return

    achou = False
    for cliente in clientes:
        if cliente["cpf"] == cpf_cliente:
            achou = True
            print("\n--- RESULTADO ---\n")
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"CPF: {cliente['cpf']}")
            break
    if not achou:
        print("Cliente não encontrado!")

def excluir_cliente(clientes):
    cpf_cliente = verificar_cpf()
    if not cpf_cliente:
        return

    removido = False
    for cliente in clientes:
        if cliente["cpf"] == cpf_cliente:
            clientes.remove(cliente)
            removido = True
            print("Removido!")
            break
    if not removido:
        print("Não há nenhum cliente cadastrado com esse CPF!")

def RegistrarEquipamentos(equipamentos: list):
    equipamento = input("Digite o nome do equipamento: ")
    quantidade = input("Digite a quantidade disponivel desse equipamento: ")
    equip = {
        "equipamento": equipamento,
        "quantidade": quantidade 
    }
    equipamentos.append(equip)

def menu_clientes(clientes: list):
    while True:
        print("\n" + "=" * 50)
        print("           SETOR CLIENTES")
        print("=" * 50)

        print("""[1] REGISTRAR CLIENTE - - - [2] EXIBIR CLIENTES
[3] PESQUISAR CLIENTE - - - [4] REMOVER CLIENTES

[0] VOLTAR""")

        opcao_clientes = int(input("Digite a opção: "))

        match opcao_clientes:

            case 1:
                registrarClientes(clientes)
            case 2:
                exibir_cliente(clientes)
            case 3:
                pesquisar_cliente(clientes)
            case 4:
                excluir_cliente(clientes)
            case 0:
                os.system('cls')
                return
            case _:
                print("ERROR! Digite uma opção entre 0 e 4.")