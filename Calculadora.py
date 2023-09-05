class CalculadoraErro(Exception):
    def __init__(self):
        super().__init__('Não é possível dividir por 0.')

class Calculadora:
    def __init__(self):
        self._registrador = 0 #Registrador para guardar os números utilizados
        self._anterior = [] # lista para guardar os numeros anteriores 

    def get_registrador(self):
        return self._registrador

    def _guarda_registrador(self):
        ''' Método para guardar os valores dentro da lista'''
        self._anterior.append(self._registrador)
        
    def adicao(self, valor: float):
        ''' Método para adição'''
        self._guarda_registrador()
        self.registrador += valor
        
    def subtracao(self, valor:float):
        ''' Método para subtração '''
        self._guarda_registrador()
        self.registrador -= valor

    def multiplicacao(self, valor:float):
        ''' Método para multiplicação '''
        self._guarda_registrador()
        self.registrador *= valor

    def divisao(self, valor:float):
        ''' Método para divisão'''
        self._guarda_registrador()
        try:
            self.registrador /= valor
        except ZeroDivisionError:
            raise CalculadoraErro
        
    def undo(self):
        ''' Método para retornar o valor guardado'''
        self.__registrador = self.__valores.pop() 
    
    def limpar(self):
        self.registrador = 0
     
    def exibe(self):
        print(self.get_registrador())

    def __str__(self) -> str:
        return f'Calculadora({self.__registrador})'