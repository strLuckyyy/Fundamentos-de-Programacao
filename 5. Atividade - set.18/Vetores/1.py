'''
1 - Implemente um programa que define um vetor de 6 posições, inicializado com zeros.
Em seguida, faça um laço que atualize o vetor de forma dinâmica com os valores [2 4
6 8 10 12], utilizando acesso indexado e uma fórmula matemática para calcular os
valores. Nenhum elemento do vetor deve deixar de ser atualizado. Depois, mostre
todo o vetor na tela;
'''

vet = [0] * 6

for i in range(6):
    vet.append((i + 1) * 2)
    vet.pop(0)
    
print(vet)
