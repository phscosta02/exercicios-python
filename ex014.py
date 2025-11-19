# Exercício 014
''' Escreva um programa que converta uma temperatura digitando em graus celsius (°c) para graus fahrenheit (°f).'''

# Solicitando temperatura em Celsius (°c)
c = float(input('Quantos graus °C: '))

# Cálculo de conversão para fahrenheit (°f)
f = 9*c/5+32

# Retornando temperatura em °c e em °f.
print(f'A temperatura {c}°c, são {f}°f')
