'''
9 - Desafio: Monte um programa onde o usuário entra com o valor das diversas notas
alcançadas por uma turma de alunos. O programa inicia perguntando o tamanho da
turma e parte para a entrada de dados. A seguir, o programa deve ser capaz de exibir
um histograma na tela, além de outras informações, conforme é mostrado a seguir:

Obs 1: Ao lado da menor e da maior nota, deve ser mostrado entre parênteses
a quantidade de vezes que essa nota apareceu;
Obs 2: Por exemplo, na linha "7.1~8.0" os 5 “*” significam que 5 alunos
alcançaram uma nota > 7.0 mas <= 8.0.

----------------------------------------------------
Resultado da avaliação da turma:
Menor nota: 2.1 (1x)
Maior nota: 10.0 (2x)
Média da turma: 6.5
Histograma das notas:
0.0 ~ 3.0: ***
3.1 ~ 4.0: **
4.1 ~ 5.0: ****
5.1 ~ 6.0: *******
6.1 ~ 7.0: **********
7.1 ~ 8.0: *****
8.1 ~ 9.0: *
9.1 ~ 10.0: **
-----------------------------------------------------
'''
def _notas(x, vNota):
    if x == 1: nota = max(vNota)
    if x == 2: nota = min(vNota)
    if x == 3: nota = sum(vNota) / tamanhoTurma
    return nota


def _quantidadeMinMaxNotas(minmaxNota, vNota):

    quantidadeNota = []

    for i in range(tamanhoTurma):
        if vNota[i] == minmaxNota: quantidadeNota.append(vNota[i])

    return len(quantidadeNota)


def _quantidadeAlunosNotas(vNota):
    
    print(vNota)

    vQNota = []
    vNota = sorted(vNota)

    nota1 = 0
    nota2 = 0
    nota3 = 0
    nota4 = 0
    nota5 = 0
    nota6 = 0
    nota7 = 0
    nota8 = 0

    for i in range(len(vNota)):
        if vNota[i] >= 0 and vNota[i] <= 3: nota1 += 1
        elif vNota[i] >= 3.1 and vNota[i] <= 4: nota2 += 1
        elif vNota[i] >= 4.1 and vNota[i] <= 5: nota3 += 1
        elif vNota[i] >= 5.1 and vNota[i] <= 6: nota4 += 1
        elif vNota[i] >= 6.1 and vNota[i] <= 7: nota5 += 1
        elif vNota[i] >= 7.1 and vNota[i] <= 8: nota6 += 1
        elif vNota[i] >= 8.1 and vNota[i] <= 9: nota7 += 1
        elif vNota[i] >= 9.1 and vNota[i] <= 10: nota8 += 1
    
    vQNota.append(nota1)
    vQNota.append(nota2)
    vQNota.append(nota3)
    vQNota.append(nota4)
    vQNota.append(nota5)
    vQNota.append(nota6) 
    vQNota.append(nota7) 
    vQNota.append(nota8)

    return vQNota
 

quantidadeAlunos = 0
vetorNotas = []
tamanhoTurma = int(input('\nQuantos alunos há na turma? '))

print('\nDigite as notas dos alunos(0 - 10):')
for contador in range(tamanhoTurma): 
    notaluno = float(input(f'Aluno {contador + 1}: '))
    if notaluno > 10: notaluno /= 10
    vetorNotas.append(notaluno)

menorNota = _notas(2, vetorNotas)
maiorNota = _notas(1, vetorNotas)
mediaTurma = _notas(3, vetorNotas)

vetorQuantNota = _quantidadeAlunosNotas(vetorNotas)

print('\n-----------------------------------------------------'
      '\nRESULTADO DA AVALIAÇÃO DA TURMA:'
      '\n'
      f'\nMenor nota: {menorNota} ({_quantidadeMinMaxNotas(menorNota, vetorNotas)}x)'
      f'\nMaior nota: {maiorNota} ({_quantidadeMinMaxNotas(maiorNota, vetorNotas)}x)'
      f'\nMédia da turma: {mediaTurma}'
      '\n'
      '\nHISTOGRAMA DAS NOTAS:'
      '\n'
      f'\n0.0 ~ 3.0: {vetorQuantNota[0]}'
      f'\n3.1 ~ 4.0: {vetorQuantNota[1]}'
      f'\n4.1 ~ 5.0: {vetorQuantNota[2]}'
      f'\n5.1 ~ 6.0: {vetorQuantNota[3]}'
      f'\n6.1 ~ 7.0: {vetorQuantNota[4]}'
      f'\n7.1 ~ 8.0: {vetorQuantNota[5]}'
      f'\n8.1 ~ 9.0: {vetorQuantNota[6]}'
      f'\n9.1 ~ 10.0: {vetorQuantNota[7]}'
      '\n-----------------------------------------------------')
