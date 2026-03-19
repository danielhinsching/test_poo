class Carro:
    def __init__(self, consumo_km_por_litro):
        self.__consumo = consumo_km_por_litro
        self.__combustivel = 0.0

    def andar(self, distancia_km):
        necessario = distancia_km / self.__consumo
        if necessario > self.__combustivel:
            km_possiveis = self.__combustivel * self.__consumo
            print(f"Combustivel insuficiente! So e possivel andar {km_possiveis:.1f} km.")
            self.__combustivel = 0
        else:
            self.__combustivel -= necessario
            print(f"Andou {distancia_km} km. Combustivel restante: {self.__combustivel:.2f} L")

    def obterGasolina(self):
        print(f"Combustivel no tanque: {self.__combustivel:.2f} L")
        return self.__combustivel

    def adicionarGasolina(self, litros):
        self.__combustivel += litros
        print(f"Abastecido com {litros} L. Total no tanque: {self.__combustivel:.2f} L")


if __name__ == "__main__":
    meuFusca = Carro(15)
    meuFusca.adicionarGasolina(20)
    meuFusca.andar(100)
    meuFusca.obterGasolina()
    meuFusca.andar(300)