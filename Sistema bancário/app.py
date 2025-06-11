


menu = """

[d] Despoitar
[s] Sacar 
[e] Extrato
[q] Sair

"""

saldo = 0
limite_valor = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ + {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Operação falho! O valor infomardo é inválido.")

    elif opcao == "s":
        valor = float(input("Infome o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_valor
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ - {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else: 
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n================== Extrato ==================")
        print("Não foram realizados movimentações" if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print ("==============================================")

    elif opcao == "q":
        print("Obrigado por utilizar o nosso serviço!")
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação")
