'''4. Solicite dois números inteiros "a" e "b" e imprima na tela se o resultado da subtração entre eles (a - b)
resulta em número positivo ou negativo. Considere o zero como positivo;'''

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

x = a - b

print('A diferença desses números é: ', x)

if x >= 0:
    print('O número é positivo.')

else: 
    print('O número é negativo.')