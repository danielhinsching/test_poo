from exercise07 import BichinhoVirtual


class BichinhoVirtualPlus(BichinhoVirtual):
    def alimentar(self, quantidade):
        nova_fome = max(0, self.getFome() - quantidade)
        self.setFome(nova_fome)
        print(f"{self.getNome()} foi alimentado! Fome atual: {self.getFome()}/10")

    def brincar(self, tempo_minutos):
        ganho_saude = min(10, self.getSaude() + tempo_minutos // 5)
        aumento_fome = min(10, self.getFome() + tempo_minutos // 10)
        self.setSaude(ganho_saude)
        self.setFome(aumento_fome)
        print(f"{self.getNome()} brincou por {tempo_minutos} min! "
              f"Saude: {self.getSaude()}/10 | Fome: {self.getFome()}/10")

    def status(self):
        print(self)

    def __str__(self):
        return (f"[{self.getNome()}] Fome:{self.getFome()}/10 | "
                f"Saude:{self.getSaude()}/10 | Humor:{self.getHumor()} | "
                f"Idade:{self.getIdade()}")


if __name__ == "__main__":
    bicho = BichinhoVirtualPlus("Rex", fome=7, saude=5)
    print(bicho)
    bicho.alimentar(3)
    bicho.brincar(30)
    print(bicho)