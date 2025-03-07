'''
7 - Alimente um vetor com 10 números e o imprima. Peça para o usuário informar um
número e o procure no vetor. Se encontrar, imprima o número lido e a(s) posição(ões)
em que foi(foram) encontrado(s). Se não encontrar, imprima o número lido e a
mensagem "NÃO ENCONTRADO";
'''

vet = []
contador = 0
loop = 0

for i in range(10): vet.append(i + 1)
print(vet)

resposta = int(input('\nDigite um número: '))

print('\nO número digitado foi: ', resposta)

while loop == 0:
    for contador in range(len(vet)):
        if resposta == vet[contador]: 
            print('\nO número digitado foi encontrado no index: ', contador)
            loop = 1
    
    if loop == 1: break

    print(f'\nO número digitado ({resposta}) não foi encontrado no vetor.')
    break
