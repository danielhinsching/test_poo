class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.__ladoA = ladoA
        self.__ladoB = ladoB

    def setLados(self, ladoA, ladoB):
        self.__ladoA = ladoA
        self.__ladoB = ladoB

    def getLadoA(self):
        return self.__ladoA

    def getLadoB(self):
        return self.__ladoB

    def calcularArea(self):
        return self.__ladoA * self.__ladoB

    def calcularPerimetro(self):
        return 2 * (self.__ladoA + self.__ladoB)


def programa_retangulo():
    print("\n=== Calculo de Pisos e Rodapes ===")
    comprimento = float(input("Informe o comprimento do local (m): "))
    largura = float(input("Informe a largura do local (m): "))

    local = Retangulo(comprimento, largura)
    area = local.calcularArea()
    perimetro = local.calcularPerimetro()

    area_piso = 0.36
    comprimento_rodape = 2.0

    qtd_pisos = -(-area // area_piso)
    qtd_rodapes = -(-perimetro // comprimento_rodape)

    print(f"\nArea do local: {area:.2f} m2")
    print(f"Perimetro do local: {perimetro:.2f} m")
    print(f"Pisos necessarios (60x60 cm): {int(qtd_pisos)} pecas")
    print(f"Rodapes necessarios (pecas de 2 m): {int(qtd_rodapes)} pecas")


if __name__ == "__main__":
    r = Retangulo(4, 6)
    print(f"Area: {r.calcularArea()} | Perimetro: {r.calcularPerimetro()}")
    programa_retangulo()