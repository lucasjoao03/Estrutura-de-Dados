class Animal:
    def __init__(self, nome, peso, posicao):
        self.__nome = nome
        self.__peso = peso
        self.__posicao = posicao

    @property
    def nome(self):
        return self.__nome
    
    @property
    def peso(self):
        return self.__peso
    
    @setter.peso()
    def peso(self, peso):
        self.__peso = peso

    @property
    def posicao(self):
        self.__posicao = posicao

    @setter.posicao()
    def posicao(self, posicao):
        self.__posicao =posicao
    
    def moverse(self):
        self.__posicao += 1