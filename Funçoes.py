def RegistrarClientes(clientes: list):
    nome = input("Digite o nome do cliente: ").upper().split()
    telefone = int(input("Digite o telefone do cliente: "))
    cpf = input("Digite o cpf do cliente: ").split()
    client = {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf
    }
    clientes.append(client)


def RegistrarEquipamentos(equipamentos: list):
    equipamento = input("Digite o nome do equipamento: ")
    quantidade = input("Digite a quantidade disponivel desse equipamento: ")
    equip = {
        "equipamento": equipamento,
        "quantidade": quantidade 
    }
    equipamentos.append(equip)
