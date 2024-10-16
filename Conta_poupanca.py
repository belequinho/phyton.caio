from Conta import ContaBancaria
class Conta_p(ContaBancaria):
    def _init_(self, numero_conta, cpf, titular, saldo=0, senha="1234"):
        super()._init_(numero_conta, cpf, titular, saldo, senha)
        self.juros = 3.5/100

    def render_juros(self, tempo):
        self.saldo += self.saldo * self.juros * tempo 
        

def transferir_conta_poupanca(valor, conta_p, conta, titular, senha):
    if conta.cpf == conta_p.cpf and conta.titular == conta_p.titular:
        conta.sacar(valor)
        conta_p.depositar(valor)

        print("Conta Corrente")
        conta.consultar_saldo()
        print("Conta Poupança")
        conta_p.consultar_saldo()
    else:
        print("conta não encontrada")
        
def transferir_poupanca_conta(valor, conta_p, conta, titular, senha):
    if conta.cpf == conta_p.cpf and conta.titular == conta_p.titular:
        conta_p.sacar(valor)
        conta.depositar(valor)

        print("Conta Corrente")
        conta.consultar_saldo()
        print("Conta Poupança")
        conta_p.consultar_saldo()
    else:
        print("conta não encontrada")
        
def to_dict(self):
    return {
            'numero_conta': self.numero_conta,
            'titular': self.titular,
            'saldo': self.saldo,
            'senha': self.senha,
            'cpf': self.cpf
        }

