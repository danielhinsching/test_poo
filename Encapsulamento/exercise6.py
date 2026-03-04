class Pessoa():
    def __init__(self, primeiroNome, ultimoNome):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

    def get_PrimeiroNome(self):
        return self.__primeiroNome

    def get_UltimoNome(self):
        return self.__ultimoNome

    def set_PrimeiroNome(self, valor):
        self.__primeiroNome = valor

    def set_UltimoNome(self, valor):
        self.__ultimoNome = valor

Pessoa1 = Pessoa("João", "Carvalho")
print(Pessoa1.get_PrimeiroNome())
print(Pessoa1.get_UltimoNome())