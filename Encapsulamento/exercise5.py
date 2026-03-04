class Laptop():
    def __init__(self, preco):
        self.__preco = preco
        
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, valor):
        self.__preco = valor
        
laptop1 = Laptop(5000)
print(laptop1.get_preco())
laptop1.set_preco(3999)
print(laptop1.get_preco())
    
    
        
