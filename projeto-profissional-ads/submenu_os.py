from sistema_ordens_de_serviço import abrir_OSs, mostrar_os, orcamento_Os, aprovar_Os, finalizar_Os, exibir_ordens, buscar_os, filtrar_ordem
from sistema_clientes import registrarClientes, exibir_cliente, pesquisar_cliente, excluir_cliente 
import os
from collections import deque

def submenu_ordens(orcamento, aprovacao, execucao, finalizados, tecnicos, clientes, estoque, id_os):

    while True:
        print("\n" + "=" * 50)
        print("               ORDENS DE SERVIÇO")
        print("=" * 50)

        print("""\n[1] - ABRIR OS - - - [2] - ORÇAMENTOS - - - [3] - APROVAR
[4] - FINALIZAR OS - - - [5] ORDENS DE SERVIÇOS - - - [6] - BUSCAR ORDEM DE SERVIÇO

[0] SAIR""")

        opcao = input("OPÇÃO DESEJADA: ")

        match opcao:
            case '1':
                id_os = abrir_OSs(orcamento, clientes, id_os)
            case '2':
                orcamento_Os(orcamento, aprovacao, estoque)
            case '3': 
                aprovar_Os(aprovacao, execucao, finalizados, tecnicos, estoque)
            case '4': 
                finalizar_Os(execucao, finalizados, clientes, tecnicos)
            case '5': 
                filtrar_ordem(orcamento, aprovacao, execucao, finalizados)
            case '6':
                buscar_os(orcamento, aprovacao, execucao, finalizados)
            case '0':
                os.system('cls')
                return id_os
            case _:
                print("ERROR! Digite um número entre 0 e 6.")



