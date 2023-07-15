class Calculadora:
    _registrador = 0
    _anterior = 0
    
    @classmethod
    def adicao(cls, valor: float):
        cls._anterior = cls._registrador
        cls._registrador += valor
        
    @classmethod
    def subtracao(cls, valor:float):
        cls._anterior = cls._registrador
        cls._registrador -= valor

    @classmethod
    def multiplicacao(cls, valor:float):
        cls._anterior = cls._registrador
        cls._registrador *= valor

    @classmethod
    def divisao(cls, valor:float):
        cls._anterior = cls._registrador
        cls._registrador /= valor

    @classmethod
    def obterRegistrador(cls) -> float:
        return cls._registrador
        
    @classmethod
    def undo(cls):
        cls._registrado = cls._anterior
    
    @classmethod
    def limpar(cls):
        cls._registrador = 0
        cls._anterior = 0
     
    @classmethod
    def exibe(cls):
        registrador = cls.obterRegistrador()
        return round(registrador, 2)