'''
7. Desenvolva um programa que solicite uma quantidade indeterminada de números positivos ao usuário, e ao
digitar o número zero, calcule e informe:
• A quantidade de números digitados
• A quantidade de pares
• A quantidade de ímpares
• A soma destes números
• A média aritmética
• O maior número
• O menor número
'''
condicao = True

soma = 0

maiorNumero = 0
menorNumero = 101

numerosDigitados = 0

quantidadeNumerosPares = 0
quantidadeNumerosImpares = 0

media = 0

print('\n Digite quantos números positivos quiser(entre 1 e 100); digite 0 para parar o loop:')

while condicao == True:
    n = int(input('\n '))

    if n == 0:
        condicao == False
        break
    else: 
        soma += n
        numerosDigitados += 1

        if n % 2 == 0:
            quantidadeNumerosPares += 1
        else:
            quantidadeNumerosImpares += 1

        if n > maiorNumero:
            maiorNumero = n
        if n < menorNumero:
            menorNumero = n


media = soma / numerosDigitados

print(f'''
    \n A quantidade de números digitados foram: {numerosDigitados}
    \n A quantidade de números pares foram: {quantidadeNumerosPares}
    \n A quantidade de números impares foram: {quantidadeNumerosImpares}
    \n A soma total dos números foram: {soma}
    \n A média aritmética foi: {media}
    \n O maior número digitado foi: {maiorNumero}
    \n O menor número digitado foi: {menorNumero}
''')
