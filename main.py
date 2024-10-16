# -*- coding: utf-8 -*-
from Banco import Banco

# Funcao para exibir o menu e obter a escolha do usuario
def exibir_menu():
    print("\n=== Banco Simulado ===")
    print("1. Criar conta corrente")
    print("2. Criar conta poupança")
    print("3. Depositar em conta corrente")
    print("4. Depositar em conta poupança")
    print("5. Sacar da conta corrente")
    print("6. Sacar da conta poupança")
    print("7. Consultar saldo da conta corrente")
    print("8. Consultar saldo da conta poupança")
    print("9. Transferir entre contas corrente")
    print("10. Transferir conta corrente para poupança")
    print("11. Transferir conta poupança para corrente")
    print("12. Sair do sistema")
    return input("Escolha uma opção: ")

# Inicializar banco
banco = Banco()

# Loop principal do programa
while True:
    opcao = exibir_menu()

    if opcao == '1':
        # Criar conta corrente
        numero_conta = int(input("Digite o número da conta: "))
        titular = input("Digite o nome do titular: ")
        cpf = input("digite seu cpf: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        senha = input("Digite uma senha para a conta: ")
        banco.criar_conta(numero_conta, cpf, titular, saldo_inicial, senha)
    
    elif opcao == '2':
        # Criar conta poupança
        numero_conta = int(input("Digite o número da conta: "))
        titular = input("Digite o nome do titular: ")
        cpf = input("digite seu cpf: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        senha = input("Digite uma senha para a conta: ")
        banco.criar_conta_p(numero_conta, cpf, titular, saldo_inicial, senha)

    elif opcao == '3':
        # Depositar em conta corrente
        numero_conta = int(input("Digite o número da conta: "))
        conta = banco.buscar_conta(numero_conta)
        if conta:
            senha = input("Digite a senha da conta: ")
            if conta.verificar_senha(senha):
                valor = float(input("Digite o valor a depositar: "))
                conta.depositar(valor)
                banco.salvar_contas()
            else:
                print("Senha incorreta.")
                
    elif opcao == '4':
        # Depositar em conta poupança
        numero_conta_p = int(input("Digite o número da conta: "))
        conta_p = banco.buscar_conta_p(numero_conta_p)
        if conta_p:
            senha = input("Digite a senha da conta: ")
            if conta_p.verificar_senha(senha):
                valor = float(input("Digite o valor a depositar: "))
                conta_p.depositar(valor)
                banco.salvar_contas_p()
            else:
                print("Senha incorreta.")

    elif opcao == '5':
        # Sacar em conta corrente
        numero_conta = int(input("Digite o número da conta: "))
        conta = banco.buscar_conta(numero_conta)
        if conta:
            senha = input("Digite a senha da conta: ")
            if conta.verificar_senha(senha):
                valor = float(input("Digite o valor a sacar: "))
                conta.sacar(valor)
                banco.salvar_contas()
            else:
                print("Senha incorreta.")
                
    elif opcao == '6':
        # Sacar em conta poupança
        numero_conta_p = int(input("Digite o número da conta: "))
        conta_p = banco.buscar_conta_p(numero_conta_p)
        if conta_p:
            senha = input("Digite a senha da conta: ")
            if conta_p.verificar_senha(senha):
                valor = float(input("Digite o valor a sacar: "))
                conta_p.sacar(valor)
                banco.salvar_contas_p()
            else:
                print("Senha incorreta.")


    elif opcao == '7':
        # Consultar saldo da conta corrente
        numero_conta = int(input("Digite o número da conta: "))
        conta = banco.buscar_conta(numero_conta)
        if conta:
            senha = input("Digite a senha da conta: ")
            if conta.verificar_senha(senha):
                conta.consultar_saldo()
            else:
                print("Senha incorreta.")
                
    elif opcao == '8':
        # Consultar saldo da conta poupança
        numero_conta_p = int(input("Digite o número da conta: "))
        conta_p = banco.buscar_conta_p(numero_conta_p)
        if conta_p:
            senha = input("Digite a senha da conta: ")
            if conta_p.verificar_senha(senha):
                conta_p.consultar_saldo()
            else:
                print("Senha incorreta.")


    elif opcao == '9':
        # Transferir entre contas correntes
        numero_conta_origem = int(input("Digite o número da conta de origem: "))
        conta_origem = banco.buscar_conta(numero_conta_origem)
        if conta_origem:
            senha = input("Digite a senha da conta de origem: ")
            if conta_origem.verificar_senha(senha):
                numero_conta_destino = int(input("Digite o número da conta de destino: "))
                conta_destino = banco.buscar_conta(numero_conta_destino)
                if conta_destino:
                    valor = float(input("Digite o valor a transferir: "))
                    conta_origem.transferir(valor, conta_destino)
                    banco.salvar_contas()
                else:
                    print("Conta de destino não encontrada.")
            else:
                print("Senha incorreta.")
        else:
            print("conta de origem não encontrada")
            
    elif opcao == '10':
        # Transferir da conta corrente para poupança
        numero_conta_origem = int(input("Digite o número da conta corrente de origem: "))
        conta_origem = banco.buscar_conta(numero_conta_origem)
        if conta_origem:
            senha = input("Digite a senha da conta de origem: ")
            if conta_origem.verificar_senha(senha):
                conta_destino = banco.buscar_conta_p(numero_conta_origem)
                if conta_destino:
                    valor = float(input("Digite o valor a transferir: "))
                    conta_origem.sacar(valor)
                    if conta_origem.saldo >=  valor: 
                        conta_destino.depositar(valor)
                        banco.salvar_contas()
                        banco.salvar_contas_p()
                else:
                    print("Conta de destino não encontrada.")
            else:
                print("Senha incorreta.")
        else:
            print("conta de origem não encontrada")
            
    elif opcao == '11':
        # Transferir da conta poupança para corrente
        numero_conta_origem = int(input("Digite o número da conta corrente de origem: "))
        conta_origem = banco.buscar_conta_p(numero_conta_origem)
        if conta_origem:
            senha = input("Digite a senha da conta de origem: ")
            if conta_origem.verificar_senha(senha):
                conta_destino = banco.buscar_conta(numero_conta_origem)
                if conta_destino:
                    valor = float(input("Digite o valor a transferir: "))
                    conta_origem.sacar(valor)
                    if conta_origem.saldo >= valor:
                        conta_destino.depositar(valor)
                        banco.salvar_contas()
                        banco.salvar_contas_p()
                else:
                    print("Conta de destino não encontrada.")
            else:
                print("Senha incorreta.")
        else:
            print("conta de origem não encontrada")
            

    elif opcao == '12':
        # Sair do programa
        print("Saindo do sistema...")
        banco.salvar_contas()
        break

    else:
        print("Opção inválida! Escolha novamente.")
