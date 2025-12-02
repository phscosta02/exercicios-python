# Exercício 032
'''Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.'''

# Importa biblioteca 
from datetime import date

# Solicita ano ao usuário
ano = int(input('Digite um ano: '))

# Verifica se o ano solicitado é bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano} Não é Bissexto.')
