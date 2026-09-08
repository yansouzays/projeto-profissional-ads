def RegistrarClientes(clientes: list):
    nome = input("Digite o nome do cliente: ").upper().strip()
    telefone = input("Digite o telefone do cliente: ")
    cpf = input("Digite o cpf do cliente: ").strip()
    client = {
        "nome": nome,
        "telefone": telefone,
        "CPF": cpf
    }
    clientes.append(client)

def exibir_cliente(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado até o momento!")
    else:
        print("\n--- LISTA DE CLIENTES ---")
        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"CPF: {cliente['CPF']}")
            print("-" * 25)

def pesquisar_cliente(clientes):
    encontrado = input("Digite o CPF do cliente que deseja encontrar: ")
    achou = False
    for cliente in clientes:
        if cliente["CPF"] == encontrado:
            achou = True
            print("\n--- RESULTADO ---\n")
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"CPF: {cliente['CPF']}")
            break
    if not achou:
        print("Cliente não encontrado!")

def excluir_cliente(clientes):
    encontrado = input("Digite o CPF do cliente que deseja encontrar: ")
    removido = False
    for cliente in clientes:
        if cliente["CPF"] == encontrado:
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

        print("\n1 - Registrar Cliente.")
        print("2 - Exibir lista de clientes.")
        print("3 - Pesquisar cliente.")
        print("4 - Remover cliente.")
        print("5 - Sair.")
        
        opcao_clientes = int(input("Digite a opção: "))

        match opcao_clientes:

            case 1:
                RegistrarClientes(clientes)
            case 2:
                exibir_cliente(clientes)
            case 3:
                pesquisar_cliente(clientes)
            case 4:
                excluir_cliente(clientes)
            case 5:
                break
            case _:
                print("ERROR! Digite uma opção válida")