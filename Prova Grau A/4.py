'''
Faça uma função que recebe por parâmetro a idade de um nadador e retorna a categoria desse nadador de acordo com a tabela abaixo. 
No “main”, solicite ao usuário que digite uma idade, use a função para identificar a categoria correspondente e de volta ao “main” imprima a categoria.

idade / categoria

0 a 4 anos / n permitido

5 a 7 anos / infantil A

8 a 10 anos / infantil B

11 a 13 anos / juvenil A

14 a 17 anos / juvenil B
'''

def idadeNadador(num):
    if num >= 0 and num <= 4:
        print("Não é permitido / Sem categoria")

    elif num >= 5 and num <= 7:
        print("Categoria Infantil A")

    elif num >= 8 and num <= 10:
        print("Categoria Infantil B")

    elif num >= 11 and num <= 13:
        print("Categoria Juvenil A")

    elif num >= 14 and num <= 17:
        print("Categoria Juvenil B")

    else:
        print("Número Invalido")


if __name__ == '__main__':
    nadador = int(input("\nQual a idade do nadador? "))
    idadeNadador(nadador)