'''
2.Declare uma função chamada “ehPositivo” que recebe um número como parâmetro. Deverá
retornar True caso o parâmetro seja positivo ou zero e retornar False caso o número seja
negativo. Crie um programa que chama a função e imprime o resultado a partir do
chamador;
'''

def ehPositivo(numero):
    if numero >= 0:
        numero = True
        return numero
    
    elif numero < 0:
        numero = False
        return numero
    
if __name__ == "__main__":
    n1 = int(input("Digite um número inteiro :"))
    print(ehPositivo(n1))