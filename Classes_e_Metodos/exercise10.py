class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        if litros > self.quantidadeCombustivel:
            print("Combustivel insuficiente na bomba!")
            return
        self.quantidadeCombustivel -= litros
        print(f"Abastecido: {litros:.2f} L por R${valor:.2f}")
        print(f"Combustivel restante na bomba: {self.quantidadeCombustivel:.2f} L")

    def abastecerPorLitro(self, litros):
        if litros > self.quantidadeCombustivel:
            print("Combustivel insuficiente na bomba!")
            return
        valor = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        print(f"Abastecido: {litros:.2f} L | Valor a pagar: R${valor:.2f}")
        print(f"Combustivel restante na bomba: {self.quantidadeCombustivel:.2f} L")

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo

    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidadeCombustivel = quantidade

    def __str__(self):
        return (f"Combustivel: {self.tipoCombustivel} | "
                f"R${self.valorLitro:.2f}/L | Estoque: {self.quantidadeCombustivel:.2f} L")


if __name__ == "__main__":
    bomba = BombaCombustivel("Gasolina", 5.89, 1000)
    print(bomba)
    bomba.abastecerPorValor(100)
    bomba.abastecerPorLitro(20)
    bomba.alterarValor(6.10)
    bomba.alterarCombustivel("Etanol")
    print(bomba)