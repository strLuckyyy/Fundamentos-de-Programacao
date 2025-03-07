'''2.Desenvolva um programa que imprima na tela uma sequência com os “n” primeiros números
naturais pares. Peça para o usuário informar o valor de “n” antes de gerar a sequência. Utilize
tanto uma estrutura contada quanto condicional'''

n = int(input('Digite um número: '))

for x in range(n + 1):
    if x % 2 == 0:
        print(x)
    x += 1

print()

i = 0
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1