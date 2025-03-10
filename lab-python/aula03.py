#Desafio
#Criar um programa para verificar a Maioridade

#passo 01: criar uma Variável
#passo 02: criar uma Estrutura de condição para verificar idade
#passo 03: Exibir a frase adequada de acordo com a idade  da pessoa.

idade = int( input("Digite sua idade"))

if idade >= 18:
    print(" Voçê é maior de idade")

elif idade >= 12:
    print("Voçê é um adolescente")

else:
    print(" Voçê é uma criança")

