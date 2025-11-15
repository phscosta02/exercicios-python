# Execício 004
''' Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
 e todas as informações possíveis sobre ele.'''

# Solicita um valor ao usuário.
variavel = input('Digite algo: ')

# Exibe características do texto informado pelo usuário
print(f'O tipo primitivo de {variavel}, é, {type(variavel)}')
print(f'Só tem espaço? {variavel.isspace()}')
print(f'É um número? {variavel.isnumeric()}')
print(f'É alfabético? {variavel.isalpha()}')
print(f'É alfanumérico? {variavel.isalnum()}')
print(f'Está em maiúscula? {variavel.isupper()}')
print(f'Está em minúscula? {variavel.islower()}')
print(f'Está capitalizada? {variavel.istitle()}')