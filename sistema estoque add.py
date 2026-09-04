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