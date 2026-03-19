class ContaCorrente:
    def __init__(self, numero, nome, saldo=0.0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def alterarNome(self, novo_nome):
        self.__nome = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de R${valor:.2f} realizado. Saldo: R${self.__saldo:.2f}")
        else:
            print("Valor invalido para deposito.")

    def saque(self, valor):
        if valor <= 0:
            print("Valor invalido para saque.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo: R${self.__saldo:.2f}")

    def __str__(self):
        return (f"Conta: {self.__numero} | Titular: {self.__nome} | "
                f"Saldo: R${self.__saldo:.2f}")


if __name__ == "__main__":
    cc = ContaCorrente(1001, "Joao Silva")
    print(cc)
    cc.deposito(500)
    cc.saque(200)
    cc.saque(400)
    cc.alterarNome("Joao S. Silva")
    print(cc)