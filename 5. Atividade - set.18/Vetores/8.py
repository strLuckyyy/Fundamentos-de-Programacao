'''
8 - Crie um programa que solicita ao usuário digitar 5 números fracionários e os
armazena em um vetor “A”. Depois, solicite mais 5 números e armazene em um
segundo vetor “B”. Mostre na tela as operações matemáticas soma, subtração,
multiplicação e divisão, índice por índice dos vetores;
'''

A = []
B = []
loop = 0

def _soma():
    for i in range(5): print(f'\nA soma dos índices {i} é: {A[i] + B[i]}')
    input()


def _subtracao(): 
    for i in range(5): print(f'\nA diferença dos índices {i} é: {A[i] - B[i]}')
    input()


def _multiplicacao():
    for i in range(5): print(f'\nO produto dos índices {i} é: {A[i] * B[i]}')
    input()


def _divisao():
    for i in range(5): print(f'\nA divisão dos índices {i} é: {A[i] / B[i]}')
    input()


if __name__ == '__main__':
    print('\nDigite 5 números fracionários: ')
    for v1 in range(5): A.append(float(input()))
    
    print('\nDigite mais 5 outros números fracionários: ')
    for v2 in range(5): B.append(float(input()))

    while loop == 0:
        print('\nSelecione uma operação: '
              '\n 1 - Soma'
              '\n 2 - Subtração'
              '\n 3 - Multiplicação'
              '\n 4 - Divisão')
        resposta = input()
        
        if resposta == '1': _soma()
        elif resposta == '2': _subtracao()
        elif resposta == '3': _multiplicacao()
        elif resposta == '4': _divisao()
        else: print('\nResposta inválida, tente novamente.')

