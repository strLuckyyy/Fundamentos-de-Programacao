caminhaoPython.py



def inserirPacote():
	pass


def retirarPacote():
	pass


def encerrarParada():
	pass


def gerarRelatório():
	pass


if __name__ == '__main__':

	Inicio do dia
		pedir o volume maximo do caminhão
		pedir o peso máximo do caminhão
	

	Realizar parada - colocar opções de escolha em loop(enquanto n for selecionado 3, repete), sendo:
		1 - inserir pacote
            O usuário deve informar o peso do pacote a ser inserido, obrigatoriamente entre 1 kg e 99 kg, e o valor
        da mercadoria;
            O sistema deve calcular e exibir ao usuário o custo do transporte, sendo R$ 1,50 por kg;
            Por padrão, a seguradora cobre apenas o valor em peso de 10 vezes o volume de carga máxima do
        caminhão. Por exemplo, no caso de um caminhão de 40 m³, o seguro cobre apenas o peso de 400 kg. A
        partir desse peso, deve ser cobrado um adicional de R$ 0,80 para cada kg excedente. O sistema deve
        perguntar se o usuário aceita o pagamento do valor extra do seguro. O pacote só pode ser embarcado no
        caminhão se a resposta for positiva.
			inserir = inserirPacote()

		2 - retirar pacote
			 localizar o último pacote carregado no caminhão e perguntar para o usuário se ele realmente
		deseja retirar o pacote de peso “p”. Caso afirmativo, o pacote deve ser retirado e descontados da carga tanto
		o peso do pacote quanto o volume (1 m³).
			retirar = retirarPacote()

		3 - encerrar parada
			encerrar = encerrarParada()


	Consultar situação
		a. Peso carregado, peso restante e peso máximo;
		b. Quantidade de pacotes carregados, quantidade de pacotes restante e quantidade máxima;
		c. Valor transportado, valor restante ou excedente e valor padrão máximo;
		
	Listar pacotes	
		vetor printado igual ao volume maximo do caminhão
		  ----
		 / |  |05|11|34|27|  |  |  |  |
		------|------------------------
		\-()--| /()\          /()()\
	

	Finalizar dia
		gerarRelatório()
			(ter propriedades na função referente aos itens abaixo, assim adicionamos em variaveis duranto o código e usamos a função para "calcular" esses dados para nos)
			a. Menor peso de pacote individual transportado durante todo o dia; *
			b. Maior peso de pacote individual transportado durante todo o dia; *

			c. Menor quantidade de pacotes embarcados em uma parada; *
			d. Maior quantidade de pacotes embarcados em uma parada; *

			e. Menor quantidade total de peso no caminhão ao encerrar parada; *
			f. Maior quantidade total de peso no caminhão ao encerrar parada; *

			g. Maior peso excedente durante todo o dia; *
			h. Maior valor excedente durante todo o dia; *
	
	Sair (como se encerra um programa?)





