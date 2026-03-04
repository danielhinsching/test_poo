class Empregado():
    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self.__salario = salario
        self.projeto = projeto
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor):
        self.__salario = valor
    
        
    def trabalho(self):
        return f"{self.nome} - {self.projeto}"
    
    def mostrar(self):
        return f"{self.nome} - {self.salario}"     

    
Empregado1 = Empregado("João", 5000, "Projeto A")
print(Empregado1.trabalho())   
