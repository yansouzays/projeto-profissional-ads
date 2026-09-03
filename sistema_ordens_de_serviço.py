from collections import deque

def mostrar_os (os_atual):
    print("\n", "-" * 40)
    print(f"\nORDEM DE SERVIÇO Nº {os_atual['id']}")
    print(f"CLIENTE: {os_atual['nome_cliente']} - - - CPF: {os_atual['cpf_cliente']}")
    print(f"APARELHO: {os_atual['aparelho']}")
    print(f'PROBLEMA: {os_atual['problema']} - - - ORÇAMENTO: {os_atual['orcamento']:.2f}')
    print("-" * 40)




def abrir_OSs (list : deque, clientes : list, proximo_id):
    print("-" * 20, "ABERTURA DE OS", "-" * 20)

    print(f"\nNUMERO DA OS: Nº {proximo_id} ")
    id_os = proximo_id
    cpf_cliente = input(f"CPF: ").upper()

    encontrado = False
    for cpf in clientes:
        if cpf_cliente == cpf['cpf']:
            nome = cpf['nome']
            telefone = cpf['telefone']
            encontrado = True
            break

    if not encontrado:
        print("CLIENTE NÃO ENCONTRADO!")
        return
    
    modelo_aparelho = input("APARELHO/MODELO: ").upper()
    problema = input("PROBLEMA: ").upper()

    orcamento = 0.0
    status = "AGUARDANDO ORÇAMENTO"

    os = {
        'id' : id_os,
        'cpf_cliente' : cpf_cliente,
        'nome_cliente' : nome,
        'telefone_cliente' : telefone,
        'aparelho' : modelo_aparelho,
        'problema' : problema,
        'orcamento' : orcamento,
        'status' : status
    }

    list.append(os)

    proximo_id += 1
    return proximo_id


def orcamento_Os (orcamentos : deque, aprovacao : deque):
    print("-" * 20, "ORÇAMENTO", "-" * 20)

    try:
        os_atual = orcamentos.popleft()
    except IndexError:
        print("FILA VAZIA!")
        return

    mostrar_os(os_atual)
    
    orcamento = float(input("\nQUANTO FICARÁ O ORÇAMENTO: R$"))
    os_atual['orcamento'] = orcamento
    os_atual['status'] = "AGUARDANDO APROVAÇÃO"
    aprovacao.append(os_atual)

def aprovar_Os (aprovacao : deque, exec : deque, final : list):
    print("-" * 20, "APROVAR ORÇAMENTO", "-" * 20)

    try:
        os_atual = aprovacao.popleft()
    except IndexError:
        print("FILA VAZIA!")
        return

    mostrar_os(os_atual)

    looping = True
    while looping: 
        try:
            aprovar = input("APROVAR ORÇAMENTO: [ Y / N ] ").upper().strip()
            if aprovar == 'Y':
                print("ORÇAMENTO ACEITO")
                os_atual['status'] = "ORÇAMENTO ACEITO, INDO PARA MANUNTEÇÃO"
                looping = False
                exec.append(os_atual)

            elif aprovar == 'N':
                print("ORÇAMENTO NEGADO")
                os_atual['status'] = "ORÇAMENTO NEGADO"
                final.append(os_atual)
                looping = False
            else:
                raise ValueError
        except ValueError:
            print("ESCOLHA UMA OPÇÃO VÁLIDA ")

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
    
    







