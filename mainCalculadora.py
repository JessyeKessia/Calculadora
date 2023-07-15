from Calculadora import Calculadora

Calculadora = Calculadora()

while True:
    print('+--------------+')
    print(f'|{Calculadora.exibe()}|')
    print('+--------------+')

    print('(+) somar')
    print('(-) subtrair')
    print('(/) dividir')
    print('(*) multiplicar')
    print('(r) resetar')
    print('(d) desfazer')
    print('(s) sair')
    print('---------------')

    escolha = input('Digite sua escolha: ').lower()

    if escolha == '+':
        valor = float(input('Digite o primeiro valor: '))
        Calculadora.adicao(valor)

    elif escolha == '-':
        valor = float(input('Digite o primeiro valor: '))
        Calculadora.subtracao(valor)

    elif escolha == '/':
        valor = float(input('Digite o primeiro valor: '))
        Calculadora.divisao(valor)

    elif escolha == '*':
        valor = float(input('Digite o primeiro valor: '))
        Calculadora.multiplicacao(valor)

    elif escolha == 'r':
        Calculadora.limpar()

    elif escolha == 'd':
        Calculadora.undo()

    elif escolha == 's':
        break

    else:
        print('Insira algo válido!')
        continue
