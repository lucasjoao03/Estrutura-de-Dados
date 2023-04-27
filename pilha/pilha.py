from no import No

class Pilha:    
    def __init__(self) -> None:
       self.topo = None
       self.tamanho = 0

    def is_empty(self):
        if self.tamanho == 0:
            return True
        return False

    def push(self, valor):
       no = No(valor) #5 #6 #7
       no.__proximo = self.topo #no #5 #6
       self.topo = no #5 #6
    
    def pop(self):
     pass
    
    def peek(self):
       pass
    def list_items(self):
      pass

    def get_size(self):
        pass