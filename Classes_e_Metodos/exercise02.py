class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
 
    def setLado(self, lado):
        self.__lado = lado
 
    def getLado(self):
        return self.__lado
 
    def calcularArea(self):
        return self.__lado ** 2
 
 
if __name__ == "__main__":
    q = Quadrado(5)
    print(f"Lado: {q.getLado()} | Area: {q.calcularArea()}")
    q.setLado(8)
    print(f"Novo lado: {q.getLado()} | Nova area: {q.calcularArea()}")
 