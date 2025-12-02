# Exercício 033
''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor. '''

# Solicita os valores ao usuário
numero_1 = int(input('Primeiro valor: '))
numero_2 = int(input('Segundo valor: '))
numero_3 = int(input('Terceiro valor: '))

# Verifica qual é o menor valor
menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

# Verifica qual é o maior valor
maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3

# Imprime o resultado
print(f'Menor valor digitado: {menor}')
print(f'Maior valor digitado: {maior}')
