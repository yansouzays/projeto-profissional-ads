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
        id_peca = int(input("informe o ID da peça: "))
    except ValueError:
        print ("Erro: o ID deve ser um numero inteiro!")
        return

    peca_encontrada = None
    for item in estoque:
        if item['id'] == id_peca:
            peca_encontrada = item
            break

    if peca_encontrada is None:
        print ("Erro: peça não encontrada no estoque!")
        return

    print(f"Peça selecionada: {peca_encontrada['nome']}")
    print(f"Quantidade em estoque:{peca_encontrada['quantidade']}")

    operacao = input("Deseja (A)dicionar ou (R)emover peças?").strip().upper()

    if operacao not in [ 'A', 'R']:
        print(" opção inválida!")
        return

    try:
        quantidade = int(input("informe a quantidade:"))
        if quantidade <= 0:
            print(" A quantidadde deve ser maior que zero!")
            return
    except ValueError:
        print("entrada inválida. Digite apenas numeros inteiros.")
        return

    if operacao == 'A':
        peca_encontrada['quantidade'] += quantidade
        print(f"Adicionadas {quantidade} unidades. Novo saldo de '{peca_encontrada['nome']}': {peca_encontrada['quantidade']}")
    elif operacao =='R':
        if quantidade > peca_encontrada['quantidade']:
            print (f"Erro: Saldo insuficiente em estoque! Saldo atual: {peca_encontrada['quantidade']}")
            return
        peca_encontrada['quantidade']-= quantidade
        print(f"removidas{quantidade} unidades. Novo saldo de '{peca_encontrada['nome']}' : {peca_encontrada['quantidade']}")

gerenciar_estoque_manual(estoque)

def cadastrar_peca(estoque: list):
    print("\n------- cadastrar peça / equipamento -------")

    try:
        id_peca = int(input(" informe o ID da peça: "))
    except ValueError:
        print("Erro: o ID deve ser um número inteiro!")
        return
    
    for item in estoque:
        if item['id'] == id_peca:
            print("Erro: já existe uma peça com esse ID!")
            return

    nome = input("Informe o nome da peça: ").strip().upper()
    categoria = input(" Informe a categoria (ex: BATERIA, FLEX, TELA): "). strip().upper()
    estado = input("Informe o estado (novo/usado): ").strip().lower()

    try:
        quantidade = int(input("Informe a Quabtidade inicial: "))
        preco = float(input("Informe o Preço (R$): "))
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
    print (f"Peça '{nome}' cadastrada com SUCESSO!")

def listar_pecas(estoque: list):

    print("\n ------- LISTA DE PEÇAS / EQUIPAMENTOS -------")
    if not estoque:
        print("Nenhuma peça cadastrada.")
        return
    print(f"{'ID':<5} | {"Nome":<30} | {'Categoria' :<12} | {'estado' :<8} | {'Quandidade':<6} | {'Preço(R$)':<10}")
    print("-" * 80)
    for item in estoque:
        print(f"{item['id']:<5}) | {item['nome']:<30} | {item['categoria']:<12} | {item['estado']:<8} | {item['quantidade']:<6} | R$ {item['preco']:<9.2f}")

def pesquisar_peca(estoque:list):
    print ("\n------- PESQUISAR PEÇA / EQUIPAMENTO -------")
    termo = input("Informe o ID ou nome para buscar: ").strip().upper()

    encontradas = []
    for item in estoque:
        if termo == str(item['id']) or termo in item['nome'].upper():
            encontradas.append(item)

    if encontradas:
        print(f"\nResultado(s) encontrado(s):")
        print(f"{'ID':<5} | {"Nome":<30} | {'Categoria' :<12} | {'estado' :<8} | {'Quandidade':<6} | {'Preço(R$)':<10}")
        print ("-" * 80)
        for item in encontradas:
             print(f"{item['id']:<5}) | {item['nome']:<30} | {item['categoria']:<12} | {item['estado']:<8} | {item['quantidade']:<6} | R$ {item['preco']:<9.2f}")

    else:
        print("Nenhuma peça encontrada com esse termo.")

def remover_peca(estoque: list):

    print ("\n------- REMOVER CADASTRO DE PEÇA -------")
    try:
        id_peca = int(input("Informw o ID da peça a ser removido:"))
    except ValueError:
        print("Erro: O ID deve ser um numero inteiro!")
        return

    for item in estoque:
        if item[item] == id_peca:
            estoque.remove(item)
            print(f" '{item['id']}' (ID: {id_peca}) removida do cadastro com SUCESSO!")
            return

    print(" Peça não encontrada no estoque.")

def menu_estoque():
    while True:
        print("\n" + "="*40)
        print("   GERENCIAMENTO DE PEÇAS / EQUIPAMENTOS")
        print("="*40)
        print("1. Cadastrar Peça/Equipamento")
        print("2. Listar Peças/Equipamentos")
        print("3. Pesquisar Peça/Equipamento")
        print("4. Remover Peça do Cadastro")
        print("5. Alterar Estoque Manual (Sua Função)")
        print("0. Voltar")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_peca(estoque)
        elif opcao == '2':
            listar_pecas(estoque)
        elif opcao == '3':
            pesquisar_peca(estoque)
        elif opcao == '4':
            remover_peca(estoque)
        elif opcao == '5':
            gerenciar_estoque_manual(estoque)
        elif opcao == '0':
            print("Saindo do gerenciamento de estoque...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_estoque()