'''
11.Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:

• Para homens: (72.7*h) - 58 (h = altura)
• Para mulheres: (62.1*h) - 44.7 (h = altura)
• Após calcular o peso ideal para a pessoa, solicite o seu peso e informe se ela está dentro da faixa ideal (peso 
+/- 5%), acima ou abaixo do peso ideal.
'''
pesoAtual: float
pesoIdeal: float

altura = float(input('\n Digite a altura em m: '))
sexo = input('\n Qual o sexo? (m/f) ')

if sexo == 'f':
    pesoIdeal = (62.1 * altura) - 44.7

if sexo == 'm':
    pesoIdeal = (72.7 * altura) - 58

pesoAtual = float(input('\n Qual o seu peso? '))
margemPeso = 5/100 * pesoIdeal

print(f'\n O peso ideal é: {pesoIdeal}')

if pesoAtual <= pesoIdeal + margemPeso and pesoAtual >= pesoIdeal - margemPeso:
    print('\nVocê está dentro da margem de peso ideal.')
    
elif pesoAtual > pesoIdeal + margemPeso:
    print('\nVocê está acima do peso ideal.')

elif pesoAtual < pesoIdeal - margemPeso:
    print('\nVocê está abaixo do peso ideal.')