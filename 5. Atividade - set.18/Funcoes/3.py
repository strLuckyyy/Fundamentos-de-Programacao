'''
3.Faça um procedimento chamado “raizes”, que recebe 3 parâmetros e calcula as raízes
conforme a fórmula de Baskara. O procedimento deverá utilizar a função “ehPositivo” para
verificar se o delta da fórmula de Baskara é positivo, e imprimir na tela as raízes calculadas
ou informar que não existem raízes. Para testar o procedimento, faça a leitura dos 3
parâmetros no “main” e em seguida chame o procedimento passando os 3 parâmetros;
'''

from cmath import sqrt

def _raizes(a, b, c):
    calculoDelta = b ** 2 - 4 * a * c
    return calculoDelta // 1

def _ehPositivo(delta):
    if delta >= 0:
        return True
    
    elif delta < 0:
        return False
   

if __name__ == "__main__":
    parA = float(input("\nInforme o valor de 'a': "))
    parB = float(input("\nInforme o valor de 'b': "))
    parC = float(input("\nInforme o valor de 'c': "))

    delta = int(_raizes(parA, parB, parC))
    verificando = _ehPositivo(delta)

    if verificando == True:
        print('\n A raiz é positiva')
        print('\n O resultado da raiz é: ', sqrt(delta))

    if verificando == False:
        print('\n Não há raiz.')
