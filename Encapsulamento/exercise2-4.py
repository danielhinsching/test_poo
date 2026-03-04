class Usuario:
    def __init__(self, primeiroNome, ultimoNome):
        self.__primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
    
    @property
    def primeiroNome(self):
        return self.__primeiroNome
    
    @primeiroNome.setter
    def primeiroNome(self, valor):
        self.__primeiroNome = valor
    
    def getPrimeiroNome(self):
        return self.__primeiroNome

usuario1 = Usuario("Joe", "Billie")
print(usuario1.primeiroNome) 