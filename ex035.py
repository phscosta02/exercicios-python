# Exercício 035
''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. '''

# Coleta o valor dos lados do triângulo
lado_1 = float(input('Primeiro valor: '))
lado_2 = float(input('Segundo valor: '))
lado_3 = float(input('Terceiro valor: '))

# Exibe se com os valores obtidos formam um triângulo
if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print(f'Os valores formam um triângulo!')
else:
    print(f'Os valores não formam um triângulo!')
