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
       no = No()
       self.topo = no
       no = self.topo.__proximo
    
    def pop(self):
     pass
    
    def peek(self):
       pass
    def list_items(self):
      pass

    def get_size(self):
        pass