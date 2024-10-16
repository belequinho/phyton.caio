class ContaBancaria:
    def __init__(self, numero_conta, cpf, titular, saldo=200, senha="1234"):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.senha = senha
        self.cpf = cpf
        
    def verificar_senha(self, senha):
        return self.senha == senha

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado: R${valor:.2f}. Saldo atual: R${self.saldo:.2f}')
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Sacado: R${valor:.2f}. Saldo atual: R${self.saldo:.2f}')
        else:
            print(f'Saque de R${valor:.2f} não permitido. Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo da conta {self.numero_conta}: R${self.saldo:.2f}')

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f'Transferido: R${valor:.2f} da conta {self.numero_conta} para a conta {conta_destino.numero_conta}.')
        else:
            print(f'Transferência de R${valor:.2f} não permitida. Saldo insuficiente.')

    def to_dict(self):
        return {
            'numero_conta': self.numero_conta,
            'titular': self.titular,
            'saldo': self.saldo,
            'senha': self.senha,
            'cpf': self.cpf
        }