'''
4 - Monte um programa que leia 10 números inteiros positivos e os armazene em um
vetor. Mostre os números na ordem inversa a que foram digitados;
'''

vet = []

for i in range(10):
    r = int(input('Digite um número: '))
    vet.append(r)

vet.reverse()
print('Ordem inversa do vetor: ', vet)
