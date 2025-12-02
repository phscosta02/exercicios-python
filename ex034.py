# Exercício 034
''' Escreva um programa que pergunte o salário de uma funcionário e calcule o valor do seu aumento. 
    Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. '''

# Solicita salário do usuário
salario = float(input('Digite seu salário atua R$'))

# Exibe o salário após calcular o aumento
if salario > 1250:
    print(f'Salário atual R${salario:.2f}\nCom aumento de 10%: R${salario*1.10:.2f}')
else:
    print(f'Salário atual R${salario:.2f}\nCom aumento de 15%: R${salario*1.15:.2f}')
