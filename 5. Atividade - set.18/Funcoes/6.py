'''
6. Desenvolva um programa que pergunte ao usuário quanto ele ganha por hora (opção 1 no menu) e o número de
horas trabalhadas no mês (opção 2 no menu). Calcule e mostre o detalhamento do seu contracheque no referido
mês, conforme o seguinte menu:

• Salário bruto (opção 3);
• Quanto pagou ao INSS (opção 4) (11%);
• Quanto pagou ao sindicato (opção 5) (2%);
• O salário líquido (opção 6);
• Sair (opção 7);
• Caso não tenha sido informado o valor recebido por hora ou a quantidade de horas trabalhadas, deve gerar
uma mensagem avisando que não há dados suficientes;
'''
import os

def _menu():
    print('----MENU----\n')
    opcao = int(input(
'''
1 - Valor da Hora
2 - Carga Horária
3 - Salário Bruto
4 - Pago ao INSS
5 - Pago ao Sindicato
6 - Salário Líquido
7 - Sair
\n'''
        ))

    return opcao


def _contracheque(x, vHora, hTrabalhada):

    salarioBruto = (vHora * hTrabalhada) * 22
    inss = 11 / 100 * salarioBruto
    sindicato = 2 / 100 * salarioBruto
    salarioLiquido = salarioBruto - inss - sindicato


    if x == 0:
        print('----------Salário Bruto----------\n'
              'R$            |   %1.2f'%salarioBruto)
    
    if x == 1:
        print('----------Valor Pago ao INSS----------\n'
              'R$            |   %1.2f'%inss)
    
    if x == 2:
        print('----------Valor Pago ao Sindicato----------\n'
              'R$            |   %1.2f'%sindicato)
        
    if x == 3:
        print('----------Salário Líquido----------\n'
              'R$            |   %1.2f'%salarioLiquido)


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clean')

    valorHora = 0.0
    horasTrabalhadas = 0
    x = 0

    loop = 1
    while loop == 1:
        os.system('cls' if os.name == 'nt' else 'clean')
        resposta = _menu()

        if resposta == 1:
            valorHora = float(input('Quando você ganha por hora? '))

        elif resposta == 2:
            horasTrabalhadas = int(input('\nQuantas horas você trabalha por dia? '))

        elif resposta > 2 and resposta != 7:
            if valorHora == 0.0 or horasTrabalhadas == 0:
                print('\nNão há dados o suficiente! \nInforme o Valor da Hora e a Carga Horária no menu.')
                input('\nAPERTE ENTER PARA CONTINUAR...')
            else:
                for i in range(3, 7):
                    if i == resposta:
                        _contracheque(x, valorHora, horasTrabalhadas)
                        input('\nAPERTE ENTER PARA CONTINUAR...')
                    x += 1
                x = 0
        elif resposta == 7:
            print('\nI-i-i-i-iisso é tudo pe-pe-pessoal!')
            os._exit(os.EX_OK)
    
    _contracheque(valorHora, horasTrabalhadas)
