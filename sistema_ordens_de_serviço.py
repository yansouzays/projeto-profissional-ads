import os
from collections import deque
import time

def mostrar_os (os_atual): #FUNÇÃO PARA IMPRIMIR ORDEM DE SERVIÇO DE FORMA PADRONIZADA
    print(f"\n{'-' * 10}ORDEM DE SERVIÇO Nº {os_atual['id']}{'-' * 10}")
    print(f"CLIENTE: {os_atual['nome_cliente']} - - - CPF: {os_atual['cpf_cliente']}")

    if os_atual['tecnico'] is None:
        os_atual['tecnico'] = "NÃO ATRIBUÍDO"
    print(f"APARELHO: {os_atual['aparelho']} - - - TECNICO RESPONSÁVEL: {os_atual['tecnico']}")
    print(f'PROBLEMA: {os_atual['problema']} - - - ORÇAMENTO: R${os_atual['orcamento']['total']:.2f}')
    print(f"PEÇAS EM ESTOQUE: ")
    for pecas in os_atual['orcamento']['peca_estoque']:
        print(f" - {pecas['nome']} - - - R${pecas['preco']}")
    print("PECAS ENCOMEDADAS: ")
    for pecas in os_atual['orcamento']['peca_fora']:
        print(f' - {pecas['nome']} - - - R${pecas['preco']}')
    print(f"VALOR DA MÃO DE OBRA: R${os_atual['orcamento']['fixo']:.2f}")
    print("-" * 40, "\n")



def abrir_OSs (orcamentos : deque, clientes : list, proximo_id): #FUNÇÃO PARA ABRIR ORDENS DE SERVIÇO
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

    nova_os = {
        'id' : id_os,
        'cpf_cliente' : cpf_cliente,
        'nome_cliente' : nome,
        'telefone_cliente' : telefone,
        'aparelho' : modelo_aparelho,
        'problema' : problema,
        'tecnico' : None,
        'orcamento' : {
            'peca_estoque' : [],
            'peca_fora' : [],
            'fixo' : 0,
            'total' : 0
                    },
        'status' : status
    }

    orcamentos.append(nova_os)
    print("\nORDEM DE SERVIÇO ABERTA COM SUCESSO!")
    
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

    valor_total = 0
    pecas_estoque = []
    pecas_encomendadas = []

    while True:
        try:
            print("DIGITE [ 0 ] PARA PULAR OU ENCERRAR ESSA ETAPA\n")
            estoque_id = int(input("DIGITE O ID DA PEÇA QUE SERÁ UTILIZADA: "))

            if estoque_id == 0:
                break

            encontrado = False
            for peca in estoque:
                if peca['id'] == estoque_id:

                    if peca['quantidade'] <= 0:
                        print("PEÇA SEM ESTOQUE!")
                        encontrado = True
                        break
                    
                    print(f"ID: {peca['id']} - - - PEÇA: {peca['nome']} - - - PREÇO UNI: R${peca['preco']}")
                    valor_total += peca['preco']
                    pecas_estoque.append(
                        {
                        'id' : peca['id'],
                        'nome' : peca['nome'],
                        'preco' : peca['preco'],
                        'quantidade' : 1
                        })
                    
                    print(f'R${valor_total}')
                    encontrado = True

            if not encontrado:
                print("PRODUTO NÃO ENCONTRADO NO SISTEMA")
        except ValueError:
            print("OPÇÃO INVÁLIDA: Digite apenas números.")

    while True:
        resposta = input("\nPEÇA ENCOMENDADA? [ S / N ] ").upper()

        if resposta == 'S':
            nome_encomendado = input("NOME DA PEÇA: ")
            valor_encomendado = float(input("VALOR DA PEÇA: R$"))
            valor_total += valor_encomendado
            pecas_encomendadas.append({
                    'nome' : nome_encomendado,
                    'preco' : valor_encomendado
                })
        elif resposta == 'N':
            break
        else:
            print("OPÇÃO INVÁLIDA! Digite S para sim ou N para Não.")

        
    valor_mao_obra = float(input("VALOR DA MÃO DE OBRA: R$"))
    valor_total += valor_mao_obra 
    os_atual['orcamento'] = {
        'peca_estoque' : pecas_estoque,
        'peca_fora' : pecas_encomendadas,
        'fixo' : valor_mao_obra,
        'total' : valor_total

    }
    os_atual['status'] = "AGUARDANDO APROVAÇÃO"
    aprovacao.append(os_atual)



def aprovar_Os (aprovacao : deque, exec : deque, final : list, tecnicos : list, estoque : list):
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

            for peca_orcamento in os_atual['orcamento']['peca_estoque']:
                for peca in estoque:
                    if peca['id'] == peca_orcamento[id]:
                        peca['quantidade'] -= peca_orcamento['quantidade']
                        break

            tecnico_responsavel = tecnicos[0]

            for tecnico in tecnicos:
                if tecnico['os_aberto'] < tecnico_responsavel['os_aberto']:
                    tecnico_responsavel = tecnico

            os_atual['tecnico'] = tecnico_responsavel['nome']
            tecnico_responsavel['os_aberto'] += 1

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



def finalizar_Os (exec : deque, finalizados : list, clientes : list, tecnicos : list):
    try:
        os_atual = exec.popleft()
    except IndexError:
        print("FILA VAZIA")
        return

    mostrar_os(os_atual)

    
    os_atual['status'] = "FINALIZADA"

    for tecnico in tecnicos:
        if tecnico['nome'] == os_atual['tecnico']:
            tecnico['os_aberto'] -= 1
            break

    finalizados.append(os_atual)

    for cpf in clientes:
        if cpf['cpf'] == os_atual['cpf_cliente']:
            cpf['historico'].append(os_atual)
            break

def exibir_ordens(lista : deque, texto : str):
    print("\n" + "=" * 50)
    print(f"               {texto}")
    print("=" * 50)

    if len(lista) == 0:
        print("\nERROR! FILA VAZIA")
        time.sleep(1)
        os.system('cls')
        return
    for ordem in lista:
        print(f'{mostrar_os(ordem)}')

    sair = input("APERTE QUALQUER E CONFIRME QUALQUER TECLA PARA VOLTAR: ")
    if sair:
        time.sleep(0.5)
        os.system('cls')
        return

def buscar_os(orcamento, aprovacao, execucao, finalizada):
    print("\n" + "=" * 50)
    print(f"               BUSCAR ORDEM DE SERVIÇO")
    print("=" * 50)

    filas = [
            orcamento,
            aprovacao,
            execucao,
            finalizada
        ]

    while True:
        try:
            print("DIGITE [0] PARA VOLTAR")
            id_os = int(input("DIGITE O ID DA ORDEM DE SERVIÇO: "))
            break
        except ValueError:
            print("ERROR! Digite apenas números.")

   

    if id_os == 0:
        return

    for fila in filas:
        for os_atual in fila:
            if os_atual['id'] == id_os:
                mostrar_os(os_atual)
                return

    print("OS NÃO ENCONTRADA")
    return None

    

  

    







