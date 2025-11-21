# Exercício 020
''' O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
    Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada. '''

# iportando biblioteca
from random import shuffle

# solicitando nome dos alunos
aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')

# listando alunos
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

# Sorteando ordem de apresentação
shuffle(lista)

# retornando a ordem definida
print(f'A ordem de apresentação sera:')
print(lista)
