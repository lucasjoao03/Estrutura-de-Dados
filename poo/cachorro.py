class Cachorro(Animal):
    def __init__(self, nome, peso, posicao):
        super.__init__(self, nome, peso, posicao)
    
    def latir(self):
        print(f" {self.nome}! Au-au...")