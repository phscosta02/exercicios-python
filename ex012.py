# Exercício 012
''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

# Solicitando preço do produto
preco = float(input('Digite o preço: '))

# Cálculo de desconto e valor economizado
desconto = preco * 0.95
abatido = preco * 0.05

# Exibindo valo com desconto e valor economizado
print(f'O valor é R${preco:.2f}, com desconto de 5% ficará R${desconto}')
print(f'Você teve economizou R${abatido}')
