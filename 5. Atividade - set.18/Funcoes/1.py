'''
1.Calculadora básica: 
Solicite ao usuário um número, um operador e em seguida outro número, por exemplo: 
   
    1 + 1 
    2.3 * 2 
    5 – 2.7 
    9.3 / 2.4

    • Interprete a expressão e dê o resultado correto;
    • Cada operação matemática deve ser uma função que retorna o resultado 
da operação para o chamador;
    • A impressão do resultado deve ser feita a partir do chamador;
'''

def Menu():
    print("\n\nInforme o operador: ")
    print(" 1. Soma \n", "2. Subtração \n", "3. Divisão \n", "4. Multiplicação \n")
    opcao = int(input())
    return opcao

def Soma(n1, n2):
    resultado = n1 + n2
    return resultado

def Subtracao(n1, n2):
    resultado = n1 - n2
    return resultado

def Divisao(n1, n2):
    resultado = n1 / n2
    return resultado

def Multiplicacao(n1, n2):
    resultado = n1 * n2
    return resultado

if __name__ == "__main__":
    numero1 = float(input("\nInforme um número para o calculo: "))
    numero2 = float(input("\nInforme outro número: "))
    operador = Menu()
    
    if operador == 1:
        print(Soma(numero1, numero2))

    elif operador == 2:
        print(Subtracao(numero1, numero2))

    elif operador == 3:
        print(Divisao(numero1, numero2))

    elif operador == 4:
        print(Multiplicacao(numero1, numero2))

    else:
        print("\nComando invalido!")