class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto({self.x}, {self.y})")


class RetanguloComPonto:
    def __init__(self, vertice_inferior_esquerdo: Ponto, largura, altura):
        self.vertice = vertice_inferior_esquerdo
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self) -> Ponto:
        cx = self.vertice.x + self.largura / 2
        cy = self.vertice.y + self.altura / 2
        return Ponto(cx, cy)

    def menu(self):
        while True:
            print("\n=== Menu Retangulo com Ponto ===")
            print("1 - Alterar vertice de origem")
            print("2 - Alterar largura e altura")
            print("3 - Mostrar centro")
            print("0 - Sair")
            op = input("Opcao: ")
            if op == "1":
                x = float(input("Novo X: "))
                y = float(input("Novo Y: "))
                self.vertice = Ponto(x, y)
            elif op == "2":
                self.largura = float(input("Nova largura: "))
                self.altura = float(input("Nova altura: "))
            elif op == "3":
                centro = self.encontrarCentro()
                print("Centro do retangulo: ", end="")
                centro.imprimir()
            elif op == "0":
                break
            else:
                print("Opcao invalida.")


if __name__ == "__main__":
    ponto = Ponto(0, 0)
    ret = RetanguloComPonto(ponto, largura=10, altura=6)
    centro = ret.encontrarCentro()
    print("Centro do retangulo: ", end="")
    centro.imprimir()
    ret.menu()