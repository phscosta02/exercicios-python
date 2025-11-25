# Exercício 026
''' Faça um programa que leia uma frase pelo teclado e mostre: 
    - Quantas vezes aparece a letra "A".
    - Em que posição ela aparece a primeira vez.
    - Em que posição ela aparece a última vez.'''

# Recebendo frase
frase = input('Digite uma frase: ').upper().strip()

# Retornando resultado
print(f'Quantidade de letra A: {frase.count('A')}')
print(f'A primeira letra A aparece: {frase.find('A')+1}')
print(f'A última letra A aparece: {frase.rfind('A')+1}')
