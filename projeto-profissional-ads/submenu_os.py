from sistema_ordens_de_serviço import abrir_OSs, mostrar_os, orcamento_Os, aprovar_Os, finalizar_Os, exibir_ordens, buscar_os
import os
from collections import deque

def submenu_ordens(orcamento, aprovacao, execucao, finalizados, tecnicos, clientes, estoque, id_os):
    while True:
        print("\n" + "=" * 50)
        print("               ORDENS DE SERVIÇO")
        print("=" * 50)

        print("""\n[1] ABRIR OS - - - [2] ORÇAMENTOS - - - [3] APROVAR
[4] FINALIZAR OS - - - [5] AGUARDANDO ORÇAMENTOS - - - [6] AGUARDADO APROVAÇÃO
[7] ORDENS EM ANDAMENTO - - - [8] OS's FINALIZADAS - - - [9] BUSCAR ORDEM DE SERVIÇO

[0] SAIR""")

        try:
            opcao = int(input("OPÇÃO DESEJADA: "))
        except ValueError:
            print("ERROR! Digite uma opção válida")

        match opcao:
            case 1:
                id_os = abrir_OSs(orcamento, clientes, id_os)
            case 2:
                orcamento_Os(orcamento, aprovacao, estoque)
            case 3: 
                aprovar_Os(aprovacao, execucao, finalizados, tecnicos, estoque)
            case 4: 
                finalizar_Os(execucao, finalizados, clientes, tecnicos)
            case 5: 
                exibir_ordens(orcamento, "AGUARDANDO ORÇAMENTO")
            case 6:
                exibir_ordens(aprovacao, "AGUARDANDO APROVACAO")
            case 7:
                exibir_ordens(execucao, "ORDENS EM ANDAMENTO")
            case 8:
                exibir_ordens(finalizados, "ORDENS FINALIZADAS")
            case 9:
                buscar_os(orcamento, aprovacao, execucao, finalizados)
            case 0:
                os.system('cls')
                return
            case _:
                print("ERROR! Digite uma opção válida")




