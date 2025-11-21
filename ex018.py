# Exercício 018
''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. '''

# Importando biblioteca
from math import radians, sin, cos, tan

# Solicitando angulo ao usuário
angulo = float(input('Digite o ângulo que você deseja: '))

# Realizando os cálculos trigonométricos
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

# Retornando resultados
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem o tangente de {tangente:.2f}')
