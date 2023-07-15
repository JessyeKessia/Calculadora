class Calculadora:
    def __init__(self):
        self.registrador = 0 #Registrador para guardar os números utilizados
        self.anterior = 0 # Numero anterior para salvar o número que estava

    def adicao(self, valor: float):
        ''' Método para adição'''
        self.anterior = self.registrador
        self.registrador += valor
        
    def subtracao(self, valor:float):
        ''' Método para subtração '''
        self.anterior = self.registrador
        self.registrador -= valor

    def multiplicacao(self, valor:float):
        ''' Método para multiplicação '''
        self.anterior = self.registrador
        self.registrador *= valor

    def divisao(self, valor:float):
        ''' Método para divisão'''
        self.anterior = self.registrador
        self.registrador /= valor

    def obterRegistrador(self) -> float:
        return self.registrador
        
    def undo(self):
        self.registrado = self.anterior
    
    def limpar(self):
        self.registrador = 0
        self.anterior = 0
     
    def exibe(self):
        registrador = self.obterRegistrador()
        return round(registrador, 2)