class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
 
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
 
    def mostraCor(self):
        print(f"A cor da bola e: {self.cor}")
 
 
if __name__ == "__main__":
    bola = Bola("vermelha", 70, "couro")
    bola.mostraCor()
    bola.trocaCor("azul")
    bola.mostraCor()