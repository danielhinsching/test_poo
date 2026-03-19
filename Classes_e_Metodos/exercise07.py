class BichinhoVirtual:
    def __init__(self, nome, fome=5, saude=10, idade=0):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    def setNome(self, nome):   self.__nome = nome
    def setFome(self, fome):   self.__fome = max(0, min(10, fome))
    def setSaude(self, saude): self.__saude = max(0, min(10, saude))
    def setIdade(self, idade): self.__idade = max(0, idade)

    def getNome(self):  return self.__nome
    def getFome(self):  return self.__fome
    def getSaude(self): return self.__saude
    def getIdade(self): return self.__idade

    def getHumor(self):
        pontuacao = self.__saude - self.__fome
        if pontuacao >= 7:
            return "Feliz"
        elif pontuacao >= 3:
            return "Normal"
        else:
            return "Mal-humorado"

    def __str__(self):
        return (f"Nome: {self.__nome} | Fome: {self.__fome}/10 | "
                f"Saude: {self.__saude}/10 | Idade: {self.__idade} | "
                f"Humor: {self.getHumor()}")


if __name__ == "__main__":
    bicho = BichinhoVirtual("Digi", fome=8, saude=3)
    print(bicho)
    bicho.setFome(4)
    bicho.setSaude(9)
    print(bicho)