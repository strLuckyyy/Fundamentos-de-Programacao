'''
3 - Monte um programa que peça para o usuário digitar 10 números fracionários, os
armazene em um vetor e em seguida mostre na tela:
2.a O índice e o conteúdo do elemento de menor valor;
2.b O índice e o conteúdo do elemento de maior valor;
2.c A diferença entre os elementos de maior e menor valor;
'''

vet = []
i = 0

print('Digite 10 numeros: ')

while i < 10:
    num = float(input(''))
    vet.append(num)
    i += 1

maxVet = max(vet)
minVet = min(vet)
difVet = maxVet - minVet

print(f'''
O menor número digitado foi:                   | {minVet}\n
O maior número digitado foi:                   | {maxVet}\n
A diferença entre os elementos acima é:        | {difVet}
''')
