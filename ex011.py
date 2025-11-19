# Exercício 011
''' Faça um programa que leia a altura e largura de uma parede em metros, calcule a quantidade de tinta necessária para pinta-la, sabendo que 1L de tinta pinta uma área de 2m². '''

# Solicitando dimensões da parede
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

# Cálculo da área, e quantidade tinta.
area = altura*largura
tinta = area / 2

# Retornando área da parede, e quanto será o consumo de tinta.
print(f'Dimensão da parede {altura}x{largura}, sua área é {area}m².')
print(f'Para pintar a parede com essa dimensão você precisará de {tinta}L de tinta')
