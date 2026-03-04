class Usuario:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    def dizer_ola(self):
        return f"Olá, {self.primeiro_nome} {self.sobrenome}!"

usuario1 = Usuario("Daniel", "Hinsching")

usuario1.primeiro_nome = "Daniel"
usuario1.sobrenome = "Hinsching"

print(usuario1.primeiro_nome)
print(usuario1.sobrenome)

print(usuario1.dizer_ola())

usuario2 = Usuario("José", "Kahl")
print(usuario2.dizer_ola())