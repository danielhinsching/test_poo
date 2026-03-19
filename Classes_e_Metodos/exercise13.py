class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = float(salario)

    def getNome(self):
        return self.__nome

    def getSalario(self):
        return self.__salario

    def aumentarSalario(self, percentual):
        self.__salario += self.__salario * (percentual / 100)

    def __str__(self):
        return f"Funcionario: {self.__nome} | Salario: R${self.__salario:.2f}"


if __name__ == "__main__":
    harry = Funcionario("Harry", 25000)
    print(harry)
    harry.aumentarSalario(10)
    print(harry)