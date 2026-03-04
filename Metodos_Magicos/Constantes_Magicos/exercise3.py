class Usuario:
    def __init__(self, primeiroNome, ultimoNome):
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
    def getNomeCompleto(self):
        return f"{self.primeiroNome} {self.ultimoNome}"

