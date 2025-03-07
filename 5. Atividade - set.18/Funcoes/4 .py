'''
4.Faça um programa que solicite ao usuário informar uma hora, minuto e segundo no
formato “hh:mm:ss”. Crie uma função chamada “horaParaFloat” que recebe esses 3
parâmetros separadamente. Essa função deverá retornar um número float
representando as horas, minutos e segundos como um número fracionário. Ex:
“01:15:30” = 1,2583 ou “13:20:15” = 13,3375. Imprima o número fracionário a partir
do “main”;
'''

def _horaParaFloat(hora, minuto, segundo):
    soma = hora + (minuto / 60) + (segundo / 3600)
    return soma


if __name__ == '__main__':
    print('Informe a hora atual: \n')

    h = int(input('hora '))
    m = int(input('minuto '))
    s = int(input('segundo '))
    i = 0

    while i == 0:
        if s >= 60:
            s -= 60
            m += 1
        elif m >= 60:
            m -= 60
            h += 1
        else:
            i = 1
            break

    print(h, ':', m, ':', s)

    soma = _horaParaFloat(h, m, s)
    print('O float da hora é: %1.4f'%soma)
