'''
2 - Implemente um programa que define um vetor vazio. Em seguida, faça um laço que
adicione no vetor os valores [-1.5 -1 -0.5 0 0.5 1 1.5 2 2.5 3] de forma dinâmica,
utilizando uma fórmula matemática para calcular os valores. Nenhum elemento do
vetor deve deixar de ser inicializado. Depois, faça outro laço que mostre todo o vetor
na tela;

'''

vet = []
i = -1.5

while i != 3.5:
    vet.append(i)
    i += 0.5

print(vet)
