# Exercício 016
''' Crei um programa que leia um número real (flutuante) qulquer e mostre na tela a sua porção inteira. '''

# Importando bilbioteca.
from math import floor

# Solicitando número ao usuário.
numero = float(input('Digite um número: '))

# Imprimindo resultados
print(f'O número real {numero}, tem como inteiro {floor(numero)}.')

# Outras formas - função trunc 
from math import trunc

# Outras formas - int
{int(numero)}