# Exercício 030
''' Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar. '''

# Solicita o valor ao usuário
numero = int(input('Digite um valor: '))

# Verifica se o número é par ou ímpar e exibe o resultado correspondente
if numero % 2 == 0:
    print(f'O número digitado é Par.')
else:
    print(f'O número digitado é Ímpar.')
