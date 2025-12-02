# Exercício 029
''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$ 7,00 por cada km acima do limite.'''

# Coleta a velocidade do veículo
radar = float(input('Digite a velocidade do carro (km/h) '))

# Retorna o valor da multa
if radar > 80:
    print(f'Você ultapassou o limite de velocidade de 80km/h')
    multa = (radar - 80) *7
    print(f'Sua velocidade foi {radar}, com multa de R${multa:.2f}')
else:
    print(f'Não ah multas nesse veiculo')
