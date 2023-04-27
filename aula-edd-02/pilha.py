class Pilha:
    def __init__(self) -> None:
        self.__pilha = []
    
    def is_empty(self):
        return True if len(self.__pilha) == 0 else False
    
    def push(self, valor):
        self.__pilha.append(valor)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!!!")
        else:
            valor = self.__pilha.pop()
            return valor
    
    def peek(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!!!")
        else:
            valor = self.__pilha.pop[-1]
            return valor
    
    def list_items(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!!!")
        else:
            print("Relação de itens na Pilha: \n")
            inverte = (self.__pilha[::-1])
            for i in inverte:
                print(i)
           

        
    def get_size(self):
        return len(self.__pilha)