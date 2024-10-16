import json 
from Conta import ContaBancaria 
from Conta_poupanca import Conta_p

class Banco:
    def __init__(self, arquivo='contas_bancarias.json', arquivo_p = "contas_poupancas.json"):
        self.arquivo = arquivo
        self.arquivo_p = arquivo_p
        self.contas = self.carregar_contas()
        self.contas_p = self.carregar_contas_p()

    def criar_conta(self, numero_conta, cpf, titular, saldo_inicial =22, senha="1234"):
        nova_conta = ContaBancaria(numero_conta, cpf, titular, saldo_inicial, senha)
        self.contas.append(nova_conta)
        self.salvar_contas()
        print(f'Conta {numero_conta} criada para {titular} com saldo inicial de R${saldo_inicial:.2f}')
    
    def criar_conta_p(self, numero_conta, cpf, titular, saldo_inicial =0, senha="1234"):
        nova_conta = Conta_p(numero_conta, cpf, titular, saldo_inicial, senha)
        self.contas_p.append(nova_conta)
        self.salvar_contas_p()
        print(f'Conta poupança {numero_conta} criada para {titular} com saldo inicial de R${saldo_inicial:.2f}')
    
    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        print(f'Conta {numero_conta} não encontrada.')
        return None
    
    def buscar_conta_p(self, numero_conta):
        for conta_p in self.contas_p:
            if conta_p.numero_conta == numero_conta:
                return conta_p
        print(f'Conta poupança {numero_conta} não encontrada.')
        return None

    def carregar_contas(self):
        try:
            with open(self.arquivo, 'r') as f:
                contas_data = json.load(f)
                return [ContaBancaria(**conta_data) for conta_data in contas_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def carregar_contas_p(self):
        try:
            with open(self.arquivo_p, 'r') as f:
                contas_p_data = json.load(f)
                return [Conta_p(**conta_data_p) for conta_data_p in contas_p_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar_contas(self):
        try:
            with open(self.arquivo, 'w') as f:
                json.dump([conta.to_dict() for conta in self.contas], f, indent=5)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def salvar_contas_p(self):
        with open(self.arquivo_p, 'w', encoding='utf-8') as f:
            json.dump([conta_p.to_dict() for conta_p in self.contas_p], f, indent=5)





















