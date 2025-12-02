# Exercício 028
''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
    qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

# Importando bibliotecas
from random import randint
from time import sleep


print('=~=' * 20)
print(f'Vou pensar em um numero de 0 a 5!')
print('=~=' * 20)

# Gera o número aleatóriamente
ia = randint(0, 5)

# Solicita ao usuário um valor entre 0 e 5
numero = int(input('Adivinhe meu número: '))

# Simula processamento (pausa de 2 segundos)
print('Processando...')
sleep(2)

# Exibe o vencedor
if numero == ia:
    print(f'PARABENS VOCÊ ACERTOU! Pensei no número {ia}.')
else:
    print(f'Você ERROU! Pensei no {ia}, e não {numero}.')
