# Exercício 015
''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
    e a quantidade de dias pelos quais ele foi alugado.
    Calcule o preço a pagar, sabendo que o carro custa R$0,15 por Km rodado.'''

# Solicitando ao usuário dias com o veículo e Km rodados
dias = int(input('Dias alugado: '))
km = float(input('Km rodados: '))

# Calcula o valor a pagar
total = (dias*60) + (km * 0.15)

# Exibe os resultados
print(f'> Dias com o veículo: {dias}\n> Km rodados {km}\n> Total a pagar R${total:.2f}')
