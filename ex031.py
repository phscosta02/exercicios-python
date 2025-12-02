# Exercício 031
''' Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
    cobrando R$0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas..'''

# Solicita a distância da viagem ao usuário
distancia = float(input('Qual foi a distância pecorrida (km): '))

# Exibe o valor da passagem, confome a distância percorrida
if distancia <= 200:
    print(f'Sua viagem é de {distancia} kmn\nO preço da sua passagem é de R${distancia*0.50:.2f}')
else: 
    print(f'Sua viagem é de {distancia} km\nO preço da sua passagem é de R${distancia*0.45:.2f}')
