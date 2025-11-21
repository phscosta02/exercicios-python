# Exercício 019
''' Um professor quer sortear um dos 4 alunos pra apagar o quadro.
    Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. '''

# improtando biblioteca
from random import choice

# solicitando nome dos alunos
aluno_1 = input('1° Aluno: ')
aluno_2 = input('2° Aluno: ')
aluno_3 = input('3° Aluno: ')
aluno_4 = input('4° Aluno: ')

# listando alunos
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

# retornando o aluno vencedor
print(f'O aluno escolhido foi {choice(lista)}')
