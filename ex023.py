# Exercício 023
''' Faça um programa que leia um número de 0 a 1999 e mostre na tela cada um dos digitos separados.
    Ex:. Digite um número: 1834
     unidade:4, dezena:3, centena:8, milhar:1 '''

# Solicitando número ao usuário
numero = int(input('Digite um valor: '))

# Calculo para definir valores numéricos
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

# Imprimindo resultado dos valores.
print(f'{unidade} unidade')
print(f'{dezena} dezena')
print(f'{centena} centena')
print(f'{milhar} milhar')
