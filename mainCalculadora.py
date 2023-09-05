import os
from calculadora import Calculadora, CalculadoraErro

# Menu
MENU_STR = """(+) somar
(-) subtrair
(/) dividir
(*) multiplicar
(r) resetar
(d) desfazer
(s) sair
"""

class InterfaceUsuario:
    def __init__(self):
        self.calculadora = Calculadora()

    def _get_valor(self):
        while True:
            try:
                return float(input("Valor: "))
            except ValueError:
                print("Valor errado. Digite novamente...")

    def exibir_menu(self) -> bool:
        self.limpar_tela()
        print("+--------------+")
        print(f"{self.calculadora.get_registrador(): >15}")
        print("+--------------+")
        print(MENU_STR)
        print("---------------")
        operacao = input("Operação: ")
        match operacao:
            case "+":
                self.calculadora.adicao(self._get_valor())
            case "-":
                self.calculadora.subtracao(self._get_valor())
            case "/":
                try:
                    self.calculadora.divisao(self._get_valor())
                except CalculadoraErro:
                    print("Impossível dividir por zero.")
            case "*":
                self.calculadora.multiplicacao(self._get_valor())
            case "r":
                self.calculadora.reset()
            case "d":
                self.calculadora.desfazer()
            case "s":
                print("Encerrando calculadora...")
                return False
            case _:
                print("Comando inválido.")
        
        return True
        
    def limpar_tela(self):
        os.system("cls")

    def executar(self):
        while self.exibir_menu():
            pass
            
if __name__ == "__main__":
    InterfaceUsuario().executar()