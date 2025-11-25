# Exercício 025
''' Crie um programa que leia o nome de uma pessoa e diga se ela possui 'Silva' no nome.'''

# Solicita nome completo do usuário
nome = input('Digite seu nome completo: ').title()

# Retorna o resultado.
print(f'Seu nome possui Silva? {'Silva' in nome}')
