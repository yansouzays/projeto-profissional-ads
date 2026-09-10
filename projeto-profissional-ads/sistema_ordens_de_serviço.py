import os
from collections import deque
from funcoes_coringas import verificar_cpf
import time

def mostrar_os (os_atual): #FUNÇÃO PARA IMPRIMIR ORDEM DE SERVIÇO DE FORMA PADRONIZADA
    print(f"\n{'-' * 10}ORDEM DE SERVIÇO Nº {os_atual['id']}{'-' * 10}")
    print(f"CLIENTE: {os_atual['nome_cliente']} - - - CPF: {os_atual['cpf_cliente']}")

    tecnico = os_atual['tecnico']
    if tecnico is None:
        tecnico = "NÃO ATRIBUIDO"
    print(f"APARELHO: {os_atual['aparelho']} - - - TECNICO RESPONSÁVEL: {tecnico}")
    print(f"PROBLEMA: {os_atual['problema']} - - - ORÇAMENTO: R${os_atual['orcamento']['total']:.2f}")
    print(f"PEÇAS EM ESTOQUE: ")
    for pecas in os_atual['orcamento']['peca_estoque']:
        print(f" - {pecas['nome']} - - - R${pecas['preco']}")
    print("PECAS ENCOMEDADAS: ")
    for pecas in os_atual['orcamento']['peca_fora']:
        print(f" - {pecas['nome']} - - - R${pecas['preco']}")
    print(f"VALOR DA MÃO DE OBRA: R${os_atual['orcamento']['fixo']:.2f}")
    print(f"STATUS: {os_atual['status']}")
    print("-" * 40, "\n")



def abrir_OSs (orcamentos : deque, clientes : list, proximo_id): #FUNÇÃO PARA ABRIR ORDENS DE SERVIÇO
    print("\n" + "=" * 50)
    print("               ABERTURA DE OS")
    print("=" * 50)

    print(f"\nNUMERO DA OS: Nº {proximo_id} ")
    id_os = proximo_id

    cpf_cliente = verificar_cpf()
    if not cpf_cliente:
        return
        
    encontrado = None
    for cliente in clientes:
        if cpf_cliente == cliente['cpf']:
            encontrado = cliente
            break

    if encontrado is None:
        print("CLIENTE NÃO ENCONTRADO!")
        return proximo_id

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

            peca = encontrar_peca(estoque, estoque_id)

            if peca is None:
                print("PRODUTO NÃO ENCONTRADO NO SISTEMA")
                continue

            if peca['quantidade'] <= 0:
                print("SEM ESTOQUE")
                continue

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

        except ValueError:
            print("OPÇÃO INVÁLIDA: Digite apenas números.")

    while True:
        resposta = input("\nPEÇA ENCOMENDADA? [ S / N ] ").upper()

        if resposta == 'S':
            nome_encomendado = input("NOME DA PEÇA: ")
            try:
                valor_encomendado = float(input("VALOR DA PEÇA: R$"))
            except ValueError:
                print("VALOR INVÁLIDO! Digite apenas números.")
                continue
            valor_total += valor_encomendado
            pecas_encomendadas.append({
                    'nome' : nome_encomendado,
                    'preco' : valor_encomendado
                })
        elif resposta == 'N':
            break
        else:
            print("OPÇÃO INVÁLIDA! Digite S para sim ou N para Não.")

    try:
        valor_mao_obra = float(input("VALOR DA MÃO DE OBRA: R$"))
    except ValueError:
        print("VALOR INVÁLIDO! Digite apenas números.")
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
                peca = encontrar_peca(estoque, peca_orcamento['id'])

                if peca:
                    peca['quantidade'] -= peca_orcamento['quantidade']

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

    confirmar = input("FINALIZAR ORDEM DE SERVIÇO? [ S / N ] ").upper().strip()
    if confirmar == 'N':
        return
    elif confirmar == 'S': 
        os_atual['status'] = "FINALIZADA"

        for tecnico in tecnicos:
            if tecnico['nome'] == os_atual['tecnico']:
                tecnico['os_aberto'] -= 1
                tecnico['os_finalizada'] += 1
                tecnico['historico'].append(os_atual['id'])
                break

        finalizados.append(os_atual)

        for cpf in clientes:
            if cpf['cpf'] == os_atual['cpf_cliente']:
                cpf['historico'].append(os_atual)
                break
    else:
        print("ERROR! Escoha uma opção válida ( S ou N )")
        return

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
        mostrar_os(ordem)

    sair = input("APERTE QUALQUER E CONFIRME QUALQUER TECLA PARA VOLTAR: ")
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

def filtrar_ordem(orcamento, aprovacao, execucao, finalizada):
    lista = [
        orcamento,
        aprovacao,
        execucao,
        finalizada
    ]

    while True:
        print("""FILTRAR POR:
    [1] - AGUARDANDO ORÇAMENTOS - - - [2] - AGUARDANDO APROVAÇÃO
    [3] - EM EXECUÇÃO       - - -     [4] - FINALIZADAS 
    
    [0] - VOLTAR""")
        opcao = input("Opção desejada: ")

        match opcao:
            case '1':
                exibir_ordens(orcamento, "AGUARDANDO ORÇAMENTO")
            case '2':
                exibir_ordens(aprovacao, "AGUARDANDO APROVAÇÃO")
            case '3':
                exibir_ordens(execucao, "EM EXECUÇÃO")
            case '4':
                exibir_ordens(finalizada, "FINALIZADAS")
            case '0':
                time.sleep(0.5)
                os.system('cls')
                return
            case _:
                print("ERROR! Digite um número entre 0 e 4.")

    
def encontrar_peca(estoque, id_peca):
    for peca in estoque:
        if peca['id'] == id_peca:
            return peca

    return None

  

    







