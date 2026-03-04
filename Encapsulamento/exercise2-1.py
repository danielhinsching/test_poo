class Usuario:
    def __init__(self, primeiroNome, ultimoNome):
        self.__primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
    
    @property
    def primeiroNome(self):
        return self.__primeiroNome
    

        