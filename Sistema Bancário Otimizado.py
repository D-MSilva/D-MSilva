class Banco:
    def __init__(self):
        self.clientes = {}
        self.contas = {}

    def cadastrar_usuario(self, cpf, nome):
        if cpf in self.clientes:
            print("CPF já cadastrado.")
        else:
            self.clientes[cpf] = nome
            print(f"Cliente {nome} cadastrado com sucesso.")

    def cadastrar_conta(self, cpf, numero_conta):
        if cpf not in self.clientes:
            print("Cliente não cadastrado.")
        elif numero_conta in self.contas:
            print("Número de conta já cadastrado.")
        else:
            self.contas[numero_conta] = {
                "cpf": cpf,
                "saldo": 0,
                "extrato": [],
                "saques_diarios": 0
            }
            print(f"Conta {numero_conta} cadastrada com sucesso para o cliente {self.clientes[cpf]}.")

    def depositar(self, numero_conta, valor):
        if numero_conta not in self.contas:
            print("Conta não encontrada.")
        elif valor <= 0:
            print("O valor do depósito deve ser positivo.")
        else:
            self.contas[numero_conta]["saldo"] += valor
            self.contas[numero_conta]["extrato"].append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, numero_conta, valor):
        if numero_conta not in self.contas:
            print("Conta não encontrada.")
        else:
            conta = self.contas[numero_conta]
            if conta["saques_diarios"] >= 3:
                print("Você já realizou 3 saques hoje. Tente novamente amanhã.")
            elif valor > 500:
                print("O valor máximo para saque é de R$ 500,00.")
            elif valor <= 0:
                print("O valor do saque deve ser positivo.")
            elif conta["saldo"] >= valor:
                conta["saldo"] -= valor
                conta["extrato"].append(f"Saque: R$ {valor:.2f}")
                conta["saques_diarios"] += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")

    def exibir_extrato(self, numero_conta):
        if numero_conta not in self.contas:
            print("Conta não encontrada.")
        else:
            conta = self.contas[numero_conta]
            if not conta["extrato"]:
                print("Não foram realizadas movimentações.")
            else:
                for movimento in conta["extrato"]:
                    print(movimento)
                print(f"Saldo atual: R$ {conta['saldo']:.2f}")

    def reset_saques_diarios(self):
        for conta in self.contas.values():
            conta["saques_diarios"] = 0


# Exemplo de uso do sistema bancário
banco = Banco()

# Cadastrar usuários
banco.cadastrar_usuario("12345678900", "João Silva")
banco.cadastrar_usuario("98765432100", "Maria Oliveira")

# Cadastrar contas
banco.cadastrar_conta("12345678900", "0001")
banco.cadastrar_conta("98765432100", "0002")

# Depósitos
banco.depositar("0001", 1000.45)
banco.depositar("0001", 500.00)

# Saques
banco.sacar("0001", 300.00)
banco.sacar("0001", 200.00)
banco.sacar("0001", 100.00)
banco.sacar("0001", 50.00)  # Excedendo o limite diário de saques

# Exibir extrato
banco.exibir_extrato("0001")

# Resetar saques diários no final do dia
banco.reset_saques_diarios()
