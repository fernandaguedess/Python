#Crie uma classe para implementar uma conta corrente.
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
#Os métodos são os seguintes: alterarNome, depósito e saque;
#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios

class ContaCorrente():
        def _init_(self,numero,nome,saldo =0):
            self.numero = numero
            self.nome=nome
            self.saldo=saldo

        def alterarNome(self, novoNome):
            self.nome=novoNome

        def depositar(self,valorDeposito):
            self.saldo = self.saldo+ valorDeposito
        def saque(self, valorSaque):
            self.saldo = self.saldo - valorSaque

conta1 = ContaCorrente ("829", "Nanda")

print(vars(conta1))

conta1.alterarNome("Nanda Guedes")
conta1.depositar(3000)
print(vars(conta1))

conta1.alterarNome("Maria Fernanda")
conta1.saque(150)
print(vars(conta1))