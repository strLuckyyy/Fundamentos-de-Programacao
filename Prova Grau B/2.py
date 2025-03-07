'''
Uma indústria produz pacotes contendo 50 unidades de parafusos, cada parafuso pesando em média 3 gramas. 
A legislação permite variação de 1 unidade para mais ou para menos em cada pacote. 
Crie uma função que recebe como parâmetro o peso de um pacote em gramas, mostra uma mensagem informando a quantidade de
parafusos contidos nele e se está aprovado ou reprovado. Por fim, a função retorna um booleano indicando se o pacote
está aprovado ou reprovado. A partir do “main”, peça para o usuário informar o peso de diversos pacotes dentro de uma 
estrutura de repetição, que só é encerrada quando digitar 0 (zero). Chame a função de validação para cada peso digitado. 
No final, mostre a quantidade total de pacotes aprovados e reprovados.
'''

def verificarPeso(peso):
    parafusos = peso / 3

    print(f'Este pacote tem, em média: {int(parafusos)} parafusos.')
    
    if 147 <= peso <= 153: return True
    else: return False


if __name__ == '__main__':
    peso = 1
    pesoTotalAp = 0
    pesoTotalRp = 0

    while peso != 0:
        peso = float(input('Qual o peso do pacote? (digite 0 para sair)'))
        analise = verificarPeso(peso)

        if analise == True: pesoTotalAp += 1; print('Peso aprovado!')
        else: pesoTotalRp += 1; print('Peso reprovado!')

    print(f'\nPacotes aprovados: {pesoTotalAp}\nPacotes reprovados: {pesoTotalRp}')  
