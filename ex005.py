# Exercício 005
''' Faça um programa que mostre um número inteiro, o seu sucessor e o antecessor.'''

# Solicita ao usuário um número para calcular valores relacionados
numero = int(input('Digite um valor: '))

# Realiza cálculos para obter o sucessor e o antecessor
sucessor = numero + 1
antecessor = numero -1

# Exibe o número digitado, seu sucessor e antecessor
print(f'O sucessor de {numero}, é {sucessor}.')
print(f'O antecessor de {numero}, é {antecessor}.')
