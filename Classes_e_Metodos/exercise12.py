class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.__saldo = saldo_inicial
        self.__taxa = taxa_juros

    def adicioneJuros(self):
        juros = self.__saldo * (self.__taxa / 100)
        self.__saldo += juros

    def getSaldo(self):
        return self.__saldo

    def __str__(self):
        return f"Saldo: R${self.__saldo:.2f} | Taxa: {self.__taxa}%"


if __name__ == "__main__":
    poupanca = ContaInvestimento(1000.0, 10)
    print(poupanca)
    for i in range(5):
        poupanca.adicioneJuros()
    print(f"Saldo apos 5 aplicacoes de juros: R${poupanca.getSaldo():.2f}")