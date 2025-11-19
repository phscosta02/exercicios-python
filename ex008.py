# Exercício 008
''' Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros. '''

# Solicita o valor em metros
mt = float(input('Digite um valor em metros: '))

# Cálculo para obter o valor em milímetros(mm) e centrimetos(cm)
mm = mt*1000
cm = mt*100

# Exibie o valor em metros(mt), milímetros(mm) e centrimetros(cm) 
print(f'{mt} metros >> {mm} milimetros.')
print(f'{mt} metros >> {cm} centimetros.')