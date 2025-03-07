'''1.Desenvolva um programa que imprima na tela uma sequência com os “n” primeiros números
naturais. Peça para o usuário informar o valor de “n” antes de gerar a sequência. Utilize tanto
uma estrutura contada quanto condicional'''

n = int(input('Digite um número: '))

for x in range(n + 1):
    print(x)
    x += 1

i = 0

print()

while i <= n:
    print(i)
    i += 1
