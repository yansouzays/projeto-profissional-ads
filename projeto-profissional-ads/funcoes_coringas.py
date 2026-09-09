import os
import time 

def verificar_cpf():
    while True:
        print("\n" + "-" * 50)
        print("Digite o CPF do cliente.")
        print("Digite [0] para cancelar.")
        print("-" * 50)

        cpf = input("INFORME O CPF: ").strip()

        if cpf == '0':
            return None

        if  cpf.isdigit() and len(cpf) == 11:
            return cpf
        
        print("CPF INVÁLIDO! Digite exatamente os 11 números.")

def verificar_tel():
    while True:
        print("\n" + "-" * 50)
        print("Digite o Telefone.")
        print("Digite [0] para cancelar.")
        print("-" * 50)

        tel = input("INFORME O TELEFONE: ").strip()

        if tel == '0':
            return None
        if tel.isdigit() and len(tel) == 11:
            return tel

        print("TELEFONE INVÁLIDO! Digite exatamente os 11 números (DDD + NÚMERO)")
        


