menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES =3

while True:

    opcao = input(menu)

    if opcao == "d": 
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"depósito r${valor:.2f} \n"
        
        else:
            print("A operaçao falhou o valor informado é inválido.")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor >  saldo
        
        execedeu_limite = valor > limite 
        
        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if  execedeu_saldo:
            print("Operação falhou! Você não tem o saldo suficiente")
        
        elif execedeu_limite:
            print("Operação falou! O valor do saque exece o limite.")

        elif execedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")
        
        elif valor > 0:
            saldo -= valor 
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação Falhou ! Valor informado é invalido")


    elif opcao == "e":
        print("\n====================== EXTRATO ===============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================================")
        

    
    elif opcao == "q":
        break

    else:
        print("Operaçao inválida, por favor selecione novamente a operaçao desejada")