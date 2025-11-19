# Exercício 010
''' Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar. '''

# Solicitando o valor em (R$) ao usuário
valor = float(input('Quanto você tem? R$'))

# Valor do dólar U$5.65
us = valor/5.65

# Retornando o valor de R$ para U$.
print(f'você possui R${valor:.2f}, e pode comprar U${us:.2f} dólares.')
