
estoque = {
    "tela display oled": 10,
    "bateria" : 12,
    "câmera frontal": 8,
    "câmera traseira": 9,
    "plaça sub de carga": 7,
    "conector de carga": 4,
    "tampa traseira de vidro" : 10,
    "placas": 15,
    "botões" : 11,
    "alto falante": 5,
} 

def gerenciar_estoque_manual():
    print("\n ---- GERENCIAMENTO DE ESTOQUE ----")
    peca = input("nome da peça:").strip()
    if peca not in estoque:
        print ("Erro: peça não encontrada no estoque!")
        return
    print(f"quantidade atual de'{peca}':{estoque[peca]}")
    operacao = input("deseja (A)dicionar ou (R)emover peças?").strip().upper()
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
        estoque[peca] += quantidade
        print(f"Adicionadas {quantidade} unidades. Novo saldo de '{peca}': {estoque[peca]}")
    elif operacao =='R':
        if quantidade > estoque[peca]:
            print (f"Erro: Saldo insuficiente em estoque! Saldo atual: {estoque[peca]}")
            return
    estoque[peca]-= quantidade
    print(f"removidas{quantidade} unidades. Novo saldo de '{peca}' : {estoque[peca]}") 

gerenciar_estoque_manual()
