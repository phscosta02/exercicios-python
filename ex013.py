# Exercício 013
''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário cin 15% de aumento.'''

# Lendo o salário do usuário
salario = float(input('Qual o seu salário? R$'))

# Cálculo do salário atual com aumento de 15%
aumento = salario * 1.15

# Retornando salário atual, e salário com reajuste
print(f'Seu salário atual é {salario:.2f}, com o resajuste de 15% ficará {aumento:.2f}')
