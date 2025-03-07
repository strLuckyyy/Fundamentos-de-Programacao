'''
5 - Monte um programa que leia 10 números inteiros positivos e os armazene em um
vetor. Crie um segundo vetor e o alimente com os valores em ordem inversa ao
primeiro. Mostre ambos na tela, percorrendo do primeiro ao último elemento;
'''

vet1 = []
vet2 = []

for i in range(10):
    x = int(input('Digite um número: '))
    vet1.append(x)
    vet2.insert(0, x)

for v1 in range(10): print(vet1[v1])
print()
for v2 in range(10): print(vet2[v2])