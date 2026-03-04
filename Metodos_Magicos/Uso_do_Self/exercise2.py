class Usuario:
    def __init__(self, primeiroNome, ultimoNome):
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
    def hello(self):
        return f"Olá,{self.primeiroNome}"