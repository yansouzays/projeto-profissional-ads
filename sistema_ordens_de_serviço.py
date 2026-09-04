from collections import deque

def mostrar_os (os_atual):
    print(f"\n{'-' * 10}ORDEM DE SERVIÇO Nº {os_atual['id']}{'-' * 10}")
    print(f"CLIENTE: {os_atual['nome_cliente']} - - - CPF: {os_atual['cpf_cliente']}")
    print(f"APARELHO: {os_atual['aparelho']}")
    print(f'PROBLEMA: {os_atual['problema']} - - - ORÇAMENTO: R${os_atual['orcamento']['total']:.2f}')
    print(f"PEÇAS EM ESTOQUE: ")
    for pecas in os_atual['orcamento']['peca_estoque']:
        print(f" - {pecas['nome']} - - - R${pecas['preco']}")
    print("PECAS ENCOMEDADAS: ")
    for pecas in os_atual['orcamento']['peca_fora']:
        print(f' - {pecas['nome']} - - - R${pecas['preco']}')
    print(f"VALOR DA MÃO DE OBRA: R${os_atual['orcamento']['fixo']:.2f}")
    print("-" * 40, "\n")


def abrir_OSs (list : deque, clientes : list, proximo_id):
    print("\n" + "=" * 50)
    print("               ABERTURA DE OS")
    print("=" * 50)

    print(f"\nNUMERO DA OS: Nº {proximo_id} ")
    id_os = proximo_id

    while True:
        print("\n" + "-" * 50)
        print("Digite o CPF do cliente")
        print("Digite [0] para cancelar")
        print("-" * 50)

        cpf_cliente = input(f"CPF: ").upper()

        if cpf_cliente == '0':
            return
        if not cpf_cliente.isdigit() or len(cpf_cliente) != 11:
            print("CPF INVÁLIDO! Digite os 11 números.")
            continue
       
        break
        
    encontrado = None
    for cliente in clientes:
        if cpf_cliente == cliente['cpf']:
            encontrado = cliente
            break

    if encontrado is None:
        print("CLIENTE NÃO ENCONTRADO!")
        return

    nome = encontrado['nome']
    telefone = encontrado['telefone']

    print("=" * 50)
    print("             CLIENTE ENCONTRADO")
    print("=" * 50)
    
    modelo_aparelho = input("APARELHO/MODELO: ").upper()
    problema = input("PROBLEMA: ").upper()
    status = "AGUARDANDO ORÇAMENTO"

    os = {
        'id' : id_os,
        'cpf_cliente' : cpf_cliente,
        'nome_cliente' : nome,
        'telefone_cliente' : telefone,
        'aparelho' : modelo_aparelho,
        'problema' : problema,
        'orcamento' : {
            'peca_estoque' : [],
            'peca_fora' : [],
            'fixo' : 0,
            'total' : 0
                    },
        'status' : status
    }

    list.append(os)

    proximo_id += 1
    return proximo_id


def orcamento_Os (orcamentos : deque, aprovacao : deque, estoque : list):
    print("\n" + "=" * 50)
    print("               ORÇAMENTO")
    print("=" * 50)

    try:
        os_atual = orcamentos.popleft()
    except IndexError:
        print("FILA VAZIA!")
        return

    mostrar_os(os_atual)

    valor_estoque = 0
    pecas_estoque = []
    pecas_fora = []

    while True:
        try:
            print("DIGITE [ 0 ] PARA PULAR OU ENCERRAR ESSA ETAPA\n")
            estoque_id = int(input("DIGITE O ID DA PEÇA QUE SERÁ UTILIZADA: "))

            if estoque_id == 0:
                break
            encontrado = False
            for id in estoque:
                if id['id'] == estoque_id:
                    print(f"ID: {id['id']} - - - PEÇA: {id['nome']} - - - PREÇO UNI: R${id['preco']}")
                    valor_estoque += id['preco']
                    pecas_estoque.append({
                        'nome' : id['nome'],
                        'preco' : id['preco']})
                    print(f'R${valor_estoque}')
                    encontrado = True

            if not encontrado:
                print("PRODUTO NÃO ENCONTRADO NO SISTEMA")
        except ValueError:
            print("OPÇÃO INVÁLIDA: Digite apenas números.")

    while True:
        resposta = input("\nPEÇA ENCOMENDADA? [ S / N ] ").upper()

        if resposta == 'S':
            nome_fora = input("NOME DA PEÇA: ")
            valor_fora = float(input("VALOR DA PEÇA: R$"))
            valor_estoque += valor_fora
            pecas_fora.append({
                    'nome' : nome_fora,
                    'preco' : valor_fora
                })
        elif resposta == 'N':
            break
        else:
            print("OPÇÃO INVÁLIDA! Digite S para sim ou N para Não.")

        
    valor_mao_obra = float(input("VALOR DA MÃO DE OBRA: R$"))
    valor_total = valor_mao_obra + valor_estoque
    os_atual['orcamento'] = {
        'peca_estoque' : pecas_estoque,
        'peca_fora' : pecas_fora,
        'fixo' : valor_mao_obra,
        'total' : valor_total

    }
    os_atual['status'] = "AGUARDANDO APROVAÇÃO"
    aprovacao.append(os_atual)

def aprovar_Os (aprovacao : deque, exec : deque, final : list):
    print("\n" + "=" * 50)
    print("               APROVAR ORÇAMENTO")
    print("=" * 50)

    try:
        os_atual = aprovacao.popleft()
    except IndexError:
        print("FILA VAZIA!")
        return

    mostrar_os(os_atual)

   
    while True: 
       
        aprovar = input("APROVAR ORÇAMENTO: [ S / N ] ").upper().strip()
        if aprovar == 'S':
            print("ORÇAMENTO ACEITO")
            os_atual['status'] = "ORÇAMENTO ACEITO, INDO PARA MANUNTEÇÃO"
            exec.append(os_atual)
            break

        elif aprovar == 'N':
            print("ORÇAMENTO NEGADO")
            os_atual['status'] = "ORÇAMENTO NEGADO"
            final.append(os_atual)
            break
        else:
            print("OPÇÃO INVÁLIDA! Digite S para sim ou N para Não.")

def finalizar_Os (exec : deque, finalizados : list, clientes : list):
    try:
        os_atual = exec.popleft()
    except IndexError:
        print("FILA VAZIA")
        return

    mostrar_os(os_atual)

    
    os_atual['status'] = "FINALIZADA"

    finalizados.append(os_atual)

    for cpf in clientes:
        if cpf['cpf'] == os_atual['cpf_cliente']:
            cpf['historico'].append(os_atual)
            break
    
    







