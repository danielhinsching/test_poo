class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        if isinstance(alimento, Macaco):
            self.bucho.extend(alimento.bucho)
            self.bucho.append(alimento.nome)
            print(f"{self.nome} comeu o macaco {alimento.nome}!")
        else:
            self.bucho.append(alimento)
            print(f"{self.nome} comeu: {alimento}")

    def verBucho(self):
        if self.bucho:
            print(f"Bucho de {self.nome}: {', '.join(self.bucho)}")
        else:
            print(f"O bucho de {self.nome} esta vazio.")

    def digerir(self):
        if self.bucho:
            digerido = self.bucho.pop(0)
            print(f"{self.nome} digeriu: {digerido}")
        else:
            print(f"{self.nome} nao tem nada para digerir.")


if __name__ == "__main__":
    m1 = Macaco("Chico")
    m2 = Macaco("Ze")

    m1.comer("banana")
    m1.comer("manga")
    m1.comer("laranja")
    m1.verBucho()
    m1.digerir()
    m1.verBucho()

    m2.comer("abacaxi")
    m2.comer(m1)
    m2.verBucho()