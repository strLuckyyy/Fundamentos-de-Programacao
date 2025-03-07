'''5. Desenvolva um programa que imprima na tela uma sequência com os “n” primeiros números fracionários 
múltiplos de 0,5 iniciando em 1,5. Peça para o usuário informar o valor de “n” antes de gerar a sequência.
Ex: “n” = 5; sequência = 1,5 2,0 2,5 3,0 3,5'''

n = int(input('Informe um número: '))

for x in range(1, n + 1):
    x -= 0.5
    print (x)
print(n)
