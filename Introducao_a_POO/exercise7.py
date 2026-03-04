class Usuario:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    def dizer_ola(self):
        return f"Olá, {self.primeiro_nome} {self.sobrenome}!"

usuario1 = Usuario("Daniel", "Hinsching")