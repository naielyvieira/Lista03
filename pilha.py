class No:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
        
    def __len__(self):
        return self.tamanho
    
    def is_empty(self):
        return self.tamanho == 0
    
    def inserir(self, valor):
        No = No(valor)
        No.proximo = self.topo
        self.topo = No
        self.tamanho += 1
    
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia!")
        valor = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor
    
    def _top(self):
        if self.size == 0:
            raise Exception("A pilha está vazia")
        return self._top.valor
    


def calcular(exp):
    p = Pilha()
    for caractere in exp:
        if caractere.isdigit():
            p.inserir(caractere)
        else:
            num2 = p.remover()
            num1 = p.remover()
            if caractere == '+':
                resultado = int(num1) + int(num2)
                p.inserir(str(resultado))
            elif caractere == '-':
                resultado = int(num1) - int(num2)
                p.inserir(str(resultado))
            elif caractere == '*':
                resultado = int(num1) * int(num2)
                p.inserir(str(resultado))
            elif caractere == "/":
                resultado = int(num1) / int(num2)
                p.inserir(str(resultado))
    return p.remover()