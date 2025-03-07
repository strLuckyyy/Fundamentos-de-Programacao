'''
6 - Monte um programa que leia 10 números inteiros positivos e os armazene em um
vetor. Reorganize o próprio vetor armazenando seus elementos em ordem inversa.
Não utilize outro vetor para isso, use apenas uma variável auxiliar. Mostre o vetor na
tela após a inversão dos elementos;
'''

vet = []

print('Digite 10 números: ')
for v1 in range(10):
    x = int(input())
    vet.insert(0, x)

for v2 in range(10): vet.reverse()

print(vet)

