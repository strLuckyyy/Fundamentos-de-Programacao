'''6. Desenvolva um programa que imprima na tela uma sequência com os “n” primeiros números fracionários 
com passo “p” iniciando em um número “i”. Peça para o usuário informar os valores de “n”, “p” e “i” antes de 
gerar a sequência.
Ex: “n” = 6, “p” = 0,3 e “i” = -1; sequência = -1,0 -0,7 -0,4 -0,1 0,2 0,5'''

n = int(input('Digite um número para a sequência: '))
p = float(input('Digite o número de passos: '))
i = float(input('Digite o número inicial: '))
r = 0

for x in range(n + 1):
    r = i - p
    print(r)
    