'''
Crie um programa que pede para o usuário informar dois números inteiros "n1" e "n2" e garanta que "n1" seja menor que "n2". 
Em seguida, chame a função "imprime", que recebe por parâmetro "n1" e "n2".
Essa função deve imprimir os valores maiores ou iguais a "n1" e menores que "n2" que produzem resto 4 ao serem divididos por 7 ou por 11.
'''

def imprime(num1, num2):
    for x in range(num1, num2 + 1):
        if x % 11 == 4 or x % 7 == 4:
            print(x)
        x += 1

if __name__ == "__main__":
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("\nDigite outro número inteiro: "))

    if n1 > n2:
        n = n1
        n1 = n2
        n2 = n

    imprime(n1, n2)
