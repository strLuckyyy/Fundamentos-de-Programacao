
print("5. Implemente um programa que solicita ao usuário o preço de um calçado e o percentual de desconto. Em"
" seguida, calcule o valor do desconto e o valor final a ser pago pelo calçado.")

print("----")
precoCalcado = float(input("Digite o preço de um calçado: "))
pDesconto = float(input("Digite o percentual de desconto: "))
pFinal = precoCalcado - (precoCalcado * (pDesconto / 100))

print("O valor descontado é: ", precoCalcado * pDesconto / 100)
print("O valor do calçado com o desconto é: ", pFinal)
