class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.crescer(0.5)

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso = max(0, self.peso - kg)

    def crescer(self, cm):
        self.altura += cm

    def __str__(self):
        return (f"Nome: {self.nome} | Idade: {self.idade} anos | "
                f"Peso: {self.peso:.1f} kg | Altura: {self.altura:.1f} cm")


if __name__ == "__main__":
    p = Pessoa("Ana", 18, 60, 165)
    print(p)
    p.envelhecer(2)
    p.engordar(3)
    print(p)
    p.emagrecer(1)
    p.crescer(2)
    print(p)