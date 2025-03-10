#Desafio
# Criar uma calculadora para realizar operações básicas de matemática
#Requisitos 
# 1 A operação matemática deve ser realizada entre 2 números
# 2 As operações básicas são : Adição, multiplicação, divisão e subtração
# 3  O programa deve tratar entrada inválidas.

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número "))
            num2 = float(input("Digite o segundo número 3"))
            operacao = input("Digite a operação(+,-,*,/):")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                 resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2
            else:
                raise ValueError
            print(f"Resultado:{resultado}")
            break
        except ValueError as e:
            print(f"Error: {e}. Tente novamente.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitido, Tente novamente")

calculadora()