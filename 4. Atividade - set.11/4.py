'''4.Desenvolva um programa que solicite um número inteiro “n” e imprima na tela o seu fatorial.
Fatorial é o produto dos números inteiros consecutivos de 1 até um dado inteiro “n”. Utilize
tanto uma estrutura contada quanto condicional'''

n = int(input('Digite um número: '))
i = 1
r = 1
r2 = 1

for x in range(1, n + 1):
    r *= x
    print(r)

print()

while i <= n:
    r2 *= i
    i += 1
    print(r2)