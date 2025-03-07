'''
Em uma eleição existem quatro candidatos, e os votos são computados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
       • 1, 2, 3, 4 = voto para os respectivos candidatos;
       • 5 = voto em branco;
       • qualquer outro valor = voto nulo


Elabore um algoritmo que repetidamente leia o código do candidato em um voto. Ao ser digitado o valor 0 (zero), encerre a leitura de votos e mostre na tela:
          a) total de votos para cada candidato;
          b) total de votos em branco;
          c) total de votos nulos;
          d) número do candidato vencedor;
'''
import os

def _titulo(txt):
    print('\n\n#### -- {0:^2} -- ####\n'.format(txt))


def _opcoes(numeroOpcao, txt: str):
    print('\n ', numeroOpcao, '- ', txt)


def _vencedor():
    # Globais
    global um, dois, tres, quatro, branco, nulo
    global vtVoto, vtNB

    #Local
    vtPro = [0]
    vtVt = [0]
    vtNm = [0]
    maxV = 0

    vtVoto.insert(0, um)
    vtVoto.insert(1, dois)
    vtVoto.insert(2, tres)
    vtVoto.insert(3, quatro)

    vtNB.insert(0, branco)
    vtNB.insert(1, nulo)

    vtPro.insert(0, um)
    vtPro.insert(1, dois)
    vtPro.insert(2, tres)
    vtPro.insert(3, quatro)


    for w in range(0, 4): print('\n Total de votos de cada candidato: {:^3} | {:^3}'.format(vtNome[w], vtVoto[w]))

    print('\n Total de votos em branco: {:^3}'
          '\n\n Total de votos nulos: {:^3}'.format(vtNB[0], vtNB[1]))
    
    for v in range(0, len(vtVoto) + 1):
        if max(vtVoto) == vtPro[v]:
            maxV = max(vtPro)
            vtVt.insert(0, maxV)
            vtNm.insert(0, vtNome[v])

    if len(vtVt) > 2:
        print('\n Os candidatos empatados são:')

        for n in range(0, len(vtVt) - 1):
            print('\n', vtVt[n], 'Votos -', vtNm[n])
        return

    else:
        for z in range(0, 4):
            if max(vtVoto) == vtVoto[z]: print('\n O vencedor é o Candidato nº {:^2} | {:^3}'.format(z + 1, vtNome[z]))


if __name__ == '__main__':
    # Globais

    # Constantes
    quantCandidatos = 6

    # Variaveis
    um = 0
    dois = 0
    tres = 0
    quatro = 0
    nulo = 0
    branco = 0
    
    # Vetores
    vtVoto = [] * 6
    vtNome = ['Putin', 'Biden', 'Enéias', 'Caneta Azul']
    vtNB = []

    LoopPrincipal = 1
    while LoopPrincipal != 0:
        os.system('cls' if os.name == 'nt' else 'clean')
        _titulo('CANDIDATOS')
        _opcoes('1', vtNome[0])
        _opcoes('2', vtNome[1])
        _opcoes('3', vtNome[2])
        _opcoes('4', vtNome[3])
        _opcoes('5', 'Branco')
        _opcoes('6', 'Nulo')
        _opcoes('0', 'Terminar a Votação')

        resposta = int(input())

        if resposta == 1: um += 1
        elif resposta == 2: dois += 1
        elif resposta == 3: tres += 1
        elif resposta == 4: quatro += 1
        elif resposta == 5: branco += 1
        elif resposta == 6: nulo += 1
        elif resposta == 0: LoopPrincipal = 0

    _vencedor()