class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print("Você já realizou 3 saques hoje. Tente novamente amanhã.")
            return

        if valor > 500:
            print("O valor máximo para saque é de R$ 500,00.")
            return

        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return

        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def exibir_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
            print(f"Saldo atual: R$ {self.saldo:.2f}")

    def reset_saques_diarios(self):
        self.saques_diarios = 0


# Exemplo de uso do sistema bancário
banco = Banco()

# Depósitos
banco.depositar(1000.45)
banco.depositar(500.00)

# Saques
banco.sacar(300.00)
banco.sacar(200.00)
banco.sacar(100.00)
banco.sacar(50.00)  # Excedendo o limite diário de saques

# Exibir extrato
banco.exibir_extrato()
