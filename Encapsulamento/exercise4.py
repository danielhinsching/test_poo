class Robo():
    def __init__(self, nome, ano_construcao):
        self.__nome = nome
        self.__ano_construcao = ano_construcao
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ano_construcao(self):
        return self.__ano_construcao
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @ano_construcao.setter
    def ano_construcao(self, valor):
        self.__ano_construcao = valor

    def diga_alo(self):
        return f"{self.nome} - {self.ano_construcao}."
    
Robo1 = Robo("Robo1", 2020)
print(Robo1.diga_alo())
        
