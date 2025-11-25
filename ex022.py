# Execício 022
''' Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas e minúsculas.
    - Quantas letras ao todo (sem considerar espaços).
    - Quantas letras tem o primeiro nome. '''

# Solicitando nome do usuário
nome = input('Digite seu nome completo: ').strip()

# Imprimindo letras em maiúsculas
print(f'Nome em maiúsculo, {nome.upper()}')

# Imprimindo letras em minúculas
print(f'Nome em minúsculo, {nome.lower()}')

# Imprimindo soma de todas as letras 
print(f'Seu nome contem, {len(nome) - nome.count(' ')} letras')

# Imprimindo quantas letras tem o primeiro nome
print(f'Primeiro nome contem, {nome.find(' ')} letras')
