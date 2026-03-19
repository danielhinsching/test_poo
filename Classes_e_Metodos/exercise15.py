import random
from exercise14 import BichinhoVirtualPlus


class FazendaBichinhos:
    def __init__(self, nomes):
        self.bichinhos = [
            BichinhoVirtualPlus(
                nome=nome,
                fome=random.randint(0, 10),
                saude=random.randint(0, 10)
            )
            for nome in nomes
        ]

    def mostrarTodos(self):
        print("\n--- Estado da Fazenda ---")
        for b in self.bichinhos:
            print(b)

    def alimentarTodos(self, quantidade):
        print(f"Alimentando todos com quantidade {quantidade}...")
        for b in self.bichinhos:
            b.alimentar(quantidade)

    def brincarComTodos(self, tempo):
        print(f"Brincando com todos por {tempo} minutos...")
        for b in self.bichinhos:
            b.brincar(tempo)

    def menu(self):
        while True:
            print("\n=== Fazenda de Bichinhos ===")
            print("1 - Ver todos os bichinhos")
            print("2 - Alimentar todos")
            print("3 - Brincar com todos")
            print("0 - Sair")
            op = input("Opcao: ")
            if op == "1":
                self.mostrarTodos()
            elif op == "2":
                qtd = int(input("Quantidade de comida (1-10): "))
                self.alimentarTodos(qtd)
            elif op == "3":
                tempo = int(input("Tempo de brincadeira (minutos): "))
                self.brincarComTodos(tempo)
            elif op == "0":
                print("Saindo da fazenda...")
                break
            else:
                print("Opcao invalida.")


if __name__ == "__main__":
    fazenda = FazendaBichinhos(["Pip", "Beep", "Zap"])
    fazenda.menu()