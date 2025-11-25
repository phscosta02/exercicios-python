# Exercício 024
''' Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra 'santo'.'''

# Solicitando nome da cidade
cidade = input('Qual a sua cidade? ').title()

# Retornando se sua cidade começa com santo.
print(f'A cidade {cidade}, Começa com Santo? {cidade [:5] == 'Santo'}')

