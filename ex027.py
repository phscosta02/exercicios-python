# Execício 027
''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    Ex.: Ana Maria Souza
    Primeiro: Ana
    Último: Maria '''

# Coletando nome do usuário
nome = input('Digite seu nome completo: ').title().split()

# Imprimindo seu primeiro nome e o último.
print(f'Seu primeiro nome: {nome[0]}\nSeu último nome: {nome[-1]}')
