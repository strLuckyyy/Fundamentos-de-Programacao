'''
5.Altere o programa anterior e adicione um procedimento chamado “floatParaHora”,
que recebe como parâmetro um número fracionário e imprime na tela as horas,
minutos e segundos correspondentes, no formato “hh:mm:ss”;
'''

def _floatParaHora(h):
    hora = 0
    min = 0
    seg = h * 3600

    i = 0
    while i == 0:
        if seg >= 60:
            seg -= 60
            min += 1
        elif min >= 60:
            min -= 60
            hora += 1
        else:
            print('O formato desse float em horas é: \n', hora, ':', min, ': %2.0f'%seg)
            i = 1
            break


if __name__ == '__main__':
    print('Informe o valor da hora em float: \n')

    hora = float(input(' '))

    _floatParaHora(hora)