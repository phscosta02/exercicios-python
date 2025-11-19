# Execício 006
''' Crie um algoritmo que leia um número inteiro e mostre seu dobro, triplo e raiz quadrada. '''

# Solicita ao usuário um número para calcular valores relacionados
numero = int(input('Digite um valor:'))

# Realiza cálculos para obter o dobro, triplo e raiz quadrada
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

# Exibe o número digitado, seu dobro, triplo e raiz quadrada 
print(f'O dobro de {numero}, é {dobro}')
print(f'O triplo de {numero}, é {triplo}')
print(f'A raiz de {numero}, é {raiz}')
