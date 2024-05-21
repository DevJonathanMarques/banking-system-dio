menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '0':
        deposito = input('Digite o valor do deposito: ')

        if float(deposito) > 0:
            saldo += float(deposito)
            extrato += f"Depósito realizado no valor de: {deposito}\n"
            print(f"Seu saldo agora é {saldo:.2f}")
        else:
            print('Digite um valor maior que zero!')

    elif opcao == '1':

        if numero_de_saques >= LIMITE_SAQUES:
            print(f'Você já alcançou o limite de saques diários')
            continue
        
        saque = input('Digite o valor do saque: ')
        
        if float(saque) <= 0:
            print("O valor deve ser maior que zero!")
            continue

        elif (saldo - float(saque)) < 0:
            print(f'Você não pode sacar esse valor, não tem saldo suficiente!')

        elif float(saque) > limite:
            print(f'O limite de saque é {limite}')

        elif float(saque) <= saldo and float(saque) <= limite and numero_de_saques < 3 and (saldo - float(saque) >= 0):
            saldo -= float(saque)
            numero_de_saques += 1
            extrato += f"Saque realizado no valor de: {saque}\n"
            print(f"Seu saldo agora é {saldo:.2f}")

        else:
            print('Ocorreu um problema!')

    elif opcao == '2':
        print(f'{extrato}') if extrato != '' else print('Não foram realizadas movimentações.')
        print(f'Saldo Atual: {saldo:.2f}')

    elif opcao == '3':
        print('Saindo do sistema. Obrigado pela preferência!')
        break

    else:
        print('Opção inválida!')