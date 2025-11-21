# Exercício 017
''' Faça um programa que leia cateto oposto e do cateto adjacente de um triângulo retângulo,
    calcule e mostre o comprimento da hipotenu.'''

# Importando biblioteca
import math

# Solicitando valores ao usuário.
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))

# Exibindo resultado.
print(f'O valor da hipotenusa é {math.hypot(co,ca):.2f}')
