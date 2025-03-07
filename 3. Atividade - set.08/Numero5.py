'''5. Solicite um número qualquer seguido de um valor inicial e um final de um intervalo. Mostre uma 
mensagem informando se o número digitado está abaixo, dentro ou acima do intervalo;'''

nQ = float(input('Digite um número qualquer: '))
vInicial = float(input('Digite um número do inicio do intervalo: '))
vFinal = float(input('Digite um número de fim do intervalo: '))

if nQ >= vInicial and nQ <= vFinal:
    print('O 1o número está dentro do intervalo.')
elif nQ < vInicial:
    print('O 1o número está abaixo do intervalo.')
elif nQ > vFinal:
    print('O 1o número está acima do intervalo.')
else: 
    print('?')