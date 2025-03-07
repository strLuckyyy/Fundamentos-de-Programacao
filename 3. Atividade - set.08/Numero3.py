'''3. Solicite dois números inteiros "a" e "b" e imprima na tela se o primeiro é perfeitamente divisível pelo
segundo (a % b), sem gerar resto;'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a % b == 0:
    print(a, 'é perfeitamente divisível por, ', b)

else:
    print('Esses númereos não são perfeitamente divisíveis')