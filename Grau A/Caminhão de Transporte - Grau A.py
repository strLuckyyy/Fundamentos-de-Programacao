import os

os.system('cls' if os.name == 'nt' else 'clean')

def _comandoInvalido():
    print('\n\nComando Inválido! Tente novamente.\n\n')
    input('\n\nAperte ENTER tecla para continuar...')


def _limparTela():
    return os.system('cls' if os.name == 'nt' else 'clean')


def _desenhoCaminhao():
    # Global
    global vtCargaCaminhao, organizado

    # Local
    chaoCaminhao = ['----' * espacoMax]
    chaoCaminhao.append('-(o)--')

    print('\n\nLista de Pacotes do Caminhão:\n'
              '\n   ------//', '| V =', espacoMax, '| P =', pesoMax, '|'
              '\n  / |[ ]||'
              '\n |  |   ||', vtCargaCaminhao,
              "\n --(O)---|", chaoCaminhao)


def _titulo(txt):
    print('\n\n#### -- {0:^2} -- ####\n'.format(txt))


def _opcoes(numeroOpcao, txt: str):
    print('\n ', numeroOpcao, '- ', txt)


def _extrato(linha: int, txt: str, simbolo: str, valor):
    if linha == 1:
        print('\n---------------------------------------------------------------')

    elif linha == 0:
        print('\n{0:<30} | {1:^2} | {2:>5}'.format(txt, simbolo, valor))


def _valorExcedente():
    
    # Global
    global vtValorCarga

    # Local
    valor = sum(vtValorCarga) - valorSeguroMax

    if valor > 0:
        return valor
    
    elif valor <= 0:
        return 0.0


def _situacaoAtual():
    # Global
    global vtValorCarga
    global pesoRestante, capacidadeRestante, valorRestante
    global pesoAtualCarregado, valorCargaTotal, quantPacotesCarregados, quantPacotesAtuais

    # Local
    valorCargaTotal = sum(vtValorCarga)
    pesoAtualCarregado = sum(vtCargaCaminhao)
    valorRestantenovo = 0

    _desenhoCaminhao()

    if valorRestante < 0:
        _extrato(1, None, None, None)
        _titulo('SITUAÇÃO ATUAL')
        _extrato(1, None, None, None)
        _extrato(0, 'Carga máxima:', 'Un', espacoMax)
        _extrato(0, 'Peso máximo:', 'Kg', pesoMax)
        _extrato(0, 'Valor cobrido pelo seguro:', 'R$', valorSeguroMax)
        _extrato(1, None, None, None)
        _extrato(0, 'Espaço de carga restante:', 'Un', capacidadeRestante)
        _extrato(0, 'Peso restante:', 'Kg', pesoRestante)
        _extrato(0, 'Valor restante:', 'R$', valorRestantenovo)
        _extrato(0, 'Valor excedente:', 'R$', _valorExcedente())
        _extrato(1, None, None, None)
        _extrato(0, 'Pacotes carregados:', 'Un', quantPacotesCarregados)
        _extrato(0, 'Pacotes atuais:', 'Un', quantPacotesAtuais)
        _extrato(0, 'Peso atual:', 'Kg', pesoAtualCarregado)
        _extrato(0, 'Valor total carregado:', 'R$', valorCargaTotal)
        _extrato(1, None, None, None)
    
    else:
        _extrato(1, None, None, None)
        _titulo('SITUAÇÃO ATUAL')
        _extrato(1, None, None, None)
        _extrato(0, 'Carga máxima:', 'Un', espacoMax)
        _extrato(0, 'Peso máximo:', 'Kg', pesoMax)
        _extrato(0, 'Valor cobrido pelo seguro:', 'R$', valorSeguroMax)
        _extrato(1, None, None, None)
        _extrato(0, 'Espaço de carga restante:', 'Un', capacidadeRestante)
        _extrato(0, 'Peso restante:', 'Kg', pesoRestante)
        _extrato(0, 'Valor restante:', 'R$', valorRestante)
        _extrato(0, 'Valor excedente:', 'R$', _valorExcedente())
        _extrato(1, None, None, None)
        _extrato(0, 'Pacotes carregados:', 'Un', quantPacotesCarregados)
        _extrato(0, 'Pacotes atuais:', 'Un', quantPacotesAtuais)
        _extrato(0, 'Peso atual:', 'Kg', pesoAtualCarregado)
        _extrato(0, 'Valor total carregado:', 'R$', valorCargaTotal)
        _extrato(1, None, None, None)

    input('\n\n Aperte ENTER para voltar ao menu...')


def _seguro(pesoCarga, valorCarga):
    # CALCULANDO SEGURO...

    # Chamando Globais:
    global valorRestante
 
    # Variáveis Locais:
    valorTaxaaPagar: float
    pesoCalculo = valorRestante - valorCarga #peso

    if pesoCalculo < 0:
        # Aplicando Taxa
        valorTaxaaPagar = pesoCarga * taxaSeguroExcedente
        return float(valorTaxaaPagar)
        
    else:
        return 0.0


def _inserirPacote():
    # INSERINDO PACOTE...
    
    # Chamando Globais:
    global vtCargaCaminhao, vtValorCarga, vtPesoProdutoPr, vtValorPr, vtPesoEncerrarProv
    global valorRestante, pesoRestante, capacidadeRestante
    global pesoAtualCarregado, quantPacotesCarregados, quantPacotesAtuais, vtValorCalculo

    # Variáveis Locais:
    resposta: str
    quantPack: int
    peso: int
    provCarregado: int
    provAtual: int
    valor: float
    taxa: float
    precoTransporte: float
    precoTotal: float
    pesoExce: float
    numero = 1

    # Loop Principal
    loopPrincipal = 't'
    while loopPrincipal == 't':
        _limparTela()
        _titulo('INSERINDO PACOTE')
        quantPack = int(input('\n\n Quantos pacotes serão transportados? '))

        if quantPack > espacoMax or quantPacotesAtuais >= espacoMax:
            print('\n\n Quantidade selecionada está acima do espaço máximo do caminhão.'
                  ' Tente novamente.')
            input('\n\n Aperte ENTER para continuar...')
            return

        i = 0
        while i < quantPack:
            print('\nInforme o peso do ', numero, 'º produto: ')
            peso = float(input())            
            valor = peso * custoTransporte

            vtValorPr.append(valor)
            vtPesoProdutoPr.append(peso)

            p = pesoRestante - sum(vtPesoProdutoPr)
            v = sum(vtValorPr)
            print('\n Peso restante: | {:^7} | {:^5}'
                  '\n Custo atual:   | {:^7} | {:^5}'.format('Kg', p, 'R$', v))

            numero += 1
            i += 1

        p = 0
        v = 0
        numero = 1

        # Caso de peso excedido:
        if sum(vtPesoProdutoPr) > pesoRestante:
            loopResposta = 't'
            while loopResposta == 't':
                
                pesoExce = pesoRestante - sum(vtPesoProdutoPr)
                print('\n\nPeso excedido! Não será possível o transporte desses produtos.')

                _extrato(1, None, None, None)
                _extrato(0, 'Peso Máximo:', 'Kg', pesoMax)
                _extrato(0, 'Peso Atual do Caminhão:', 'Kg', pesoAtualCarregado)
                _extrato(0, 'Peso Total das Mercadorias:', 'Kg', sum(vtPesoProdutoPr))
                _extrato(0, 'Peso Excedido:', 'Kg', pesoExce)
                _extrato(1, None, None, None)

                _opcoes('1', 'Voltar ao Menu')
                _opcoes('2', 'Trocar Produtos')

                resposta = input()
                
                if resposta == '1':
                    vtPesoProdutoPr.clear()
                    vtValorPr.clear()
                    return

                elif resposta == '2':
                    vtPesoProdutoPr.clear()
                    vtValorPr.clear()

                    loopResposta = 'f'
                    loopPrincipal = 't'
                    break
                
                else:
                    _comandoInvalido()
                    loopResposta = 't'
        else:
            loopPrincipal = 'f'
            continue
                
    taxa = _seguro(sum(vtPesoProdutoPr), sum(vtValorPr))
    precoTransporte = sum(vtPesoProdutoPr) * custoTransporte
    precoTotal = precoTransporte + taxa

    _titulo('EXTRATO')
    _extrato(1, None, None, None)
    _extrato(0, 'Peso da Mercadoria:', 'Kg', sum(vtPesoProdutoPr))
    _extrato(0, 'Preço do Transporte:', 'R$', precoTransporte)
    _extrato(1, None, None, None)
    _extrato(0, 'Taxa do Seguro:', 'R$', taxa)
    _extrato(1, None, None, None)
    _extrato(0, 'Valor Total:', 'R$', precoTotal)
    _extrato(1, None, None, None)

    loopResposta = 't'
    while loopResposta == 't':
        print('\n\nConfirmar pagamento?(s/n) ')
        resposta = input()

        if resposta == 's':
            provCarregado = quantPacotesCarregados
            provAtual = quantPacotesAtuais

            for x in range(len(vtPesoProdutoPr)):
                vtCargaCaminhao.insert(x, vtPesoProdutoPr[x])
                if vtCargaCaminhao[0 - 1] == 0: vtCargaCaminhao.remove(0)

                vtValorCarga.insert(x, vtValorPr[x])
                if vtValorCarga[0 - 1] == 0.0: vtValorCarga.remove(0.0)

                quantPacotesCarregados += 1
                quantPacotesAtuais += 1                

            # Referente ao Relatorio
            vtQuantEmbarcadosParada.insert(0, len(vtPesoProdutoPr))
            vtPesoEncerrarProv.insert(0, sum(vtPesoProdutoPr))
            if vtPesoEncerrarProv[0 - 1] == 0.0: vtPesoEncerrarProv.remove(0.0) 
            vtPesoTotalDia.extend(vtPesoProdutoPr)

            pe = taxa / taxaSeguroExcedente - pesoSeguroMax
            for r in range(0, quantPack):
                vtPesoExcedido.insert(r, pe)
                vtValorExcedido.insert(r, taxa)
            # ----------------------

            if quantPacotesAtuais == provAtual: quantPacotesAtuais += 1
            if quantPacotesCarregados == provCarregado: quantPacotesCarregados += 1

            vtPesoProdutoPr.clear()
            vtValorPr.clear()
            pesoRestante = pesoMax
            capacidadeRestante = espacoMax

            capacidadeRestante -= quantPacotesAtuais
            valorRestante -= sum(vtValorCarga)
            pesoRestante -= sum(vtCargaCaminhao)
            
            if pesoRestante < 0:
                pesoRestante *= -1
            return

        elif resposta == 'n':
            _opcoes('1', 'Voltar ao Menu')
            _opcoes('2', 'Trocar Produtos')
            vtPesoProdutoPr.clear
            vtValorPr.clear
            resposta = input()
                
            if resposta == '1':
                return

            elif resposta == '2':
                loopResposta = 'f'
                break
                
            else:
                _comandoInvalido()
                loopResposta = 't'
            
        else:
            _comandoInvalido()
            loopResposta = 't'


def _retirarPacote():
    # RETIRANDO PACOTE...
    
    # Globais
    global vtCargaCaminhao, vtValorCarga
    global pesoRestante, valorRestante, capacidadeRestante
    global pesoAtualCarregado, quantPacotesAtuais, valorCargaTotal
    
    # Locais
    pesoAtualCarregado = sum(vtCargaCaminhao)
    vetorNumero = [0] * espacoMax
    peso: int
    valor: float
    resposta: any

    for y in range(0, espacoMax):
        vetorNumero.append(y + 1)
        vetorNumero.pop(0)

    _titulo('RETIRANDO PACOTE')
    print('\nQuantos pacotes serão retirados?')
    r = int(input(': '))

    if r == espacoMax:
        for x in range(0, espacoMax):
            peso = vtCargaCaminhao[0]
            valor = (vtCargaCaminhao[0]) * custoTransporte

            vtCargaCaminhao.pop(0)
            vtCargaCaminhao.append(0)

            vtValorCarga.pop(0)
            vtValorCarga.append(0.0)

            pesoAtualCarregado -= peso
            quantPacotesAtuais -= 1
            valorCargaTotal -= valor

            pesoRestante += peso
            valorRestante += valor
            capacidadeRestante += 1
        print('\n', vtCargaCaminhao)
        print('\n\n O caminhão foi esvaziado com sucesso!\n')
        input('\nPressione ENTER para continuar...')
        return

    for x in range(0, r):
        print('\nQual pacote você deseja retirar?(digite o número correspondente)')
        print('\n', vtCargaCaminhao)
        print('\n', vetorNumero)
        resposta = int(input(': '))
        
        for x in range(0, espacoMax):
            if x == resposta - 1:
                peso = vtCargaCaminhao[x]
                valor = (vtCargaCaminhao[x]) * custoTransporte

                vtCargaCaminhao.pop(x)
                vtCargaCaminhao.append(0)

                pesoAtualCarregado -= peso
                quantPacotesAtuais -= 1
                valorCargaTotal -= valor

                pesoRestante += peso
                valorRestante += valor
                capacidadeRestante += 1
                break

    _desenhoCaminhao()
    input('\nAperte ENTER para continuar...')  


def _relatorio():
    # GERANDO RELATÓRIO...

    # Globais
    global vtPesoTotalDia, vtQuantEmbarcadosParada, vtPesoTotalEncerrarParada, vtPesoExcedido, vtValorExcedido, vtValorCalculo

    # Local
    if min(vtPesoTotalDia) == 0.0: vtPesoTotalDia.remove(0.0)
    if min(vtQuantEmbarcadosParada) == 0: vtQuantEmbarcadosParada.remove(0)
    if min(vtPesoTotalEncerrarParada) == 0.0: vtPesoTotalEncerrarParada.remove(0.0)

    menorPeso = min(vtPesoTotalDia)
    maiorPeso = max(vtPesoTotalDia)

    menorUnidade = min(vtQuantEmbarcadosParada)
    maiorUnidade = max(vtQuantEmbarcadosParada)

    menorPesoEncerrar = min(vtPesoTotalEncerrarParada)
    maiorPesoEncerrar = max(vtPesoTotalEncerrarParada)

    maiorPesoExcedido = max(vtPesoExcedido)
    maiorValorExcedido = max(vtValorExcedido)

    _titulo('RELATÓRIO DO DIA')
    _extrato(1, None, None, None)
    _extrato(0, 'Menor peso de pacote individual transportado durante todo o dia', 'Kg', menorPeso)
    _extrato(0, 'Maior peso de pacote individual transportado durante todo o dia', 'Kg', maiorPeso)
    _extrato(1, None, None, None)
    _extrato(0, 'Menor quantidade de pacotes embarcados em uma parada', 'Un', menorUnidade)
    _extrato(0, 'Maior quantidade de pacotes embarcados em uma parada', 'Un', maiorUnidade)
    _extrato(1, None, None, None)
    _extrato(0, 'Menor quantidade total de peso no caminhão ao encerrar parada', 'Kg', menorPesoEncerrar)
    _extrato(0, 'Maior quantidade total de peso no caminhão ao encerrar parada', 'Kg', maiorPesoEncerrar)
    _extrato(1, None, None, None)
    _extrato(0, 'Maior peso excedente durante todo o dia', 'Kg', maiorPesoExcedido)
    _extrato(0, 'Maior valor excedente durante todo o dia', 'R$', maiorValorExcedido)
    _extrato(1, None, None, None)


if __name__ == '__main__':
    
    # Globais:
    # Constantes
    espacoMax = int(input('\n\n Qual o volume máximo que o caminhão suporta?(m³) '))
    pesoMax = int(input('\n Qual peso máximo que o caminhão suporta?(Kg) '))
    custoTransporte = 1.5
    pesoSeguroMax = espacoMax * 10
    valorSeguroMax = pesoSeguroMax * custoTransporte
    taxaSeguroExcedente = 0.8

    # Vetores
    vtCargaCaminhao = [0] * espacoMax
    vtValorCarga = [0.0] * espacoMax

    vtPesoProdutoPr = []
    vtValorPr = []

    vtPesoTotalDia = [0.0]
    vtQuantEmbarcadosParada = [0]
    vtPesoTotalEncerrarParada = [0.0]
    vtPesoEncerrarProv = [0.0]
    vtPesoExcedido = [0.0]
    vtValorExcedido = [0.0]
    vtValorCalculo = [0]

    # Variáveis
    quantPacotesCarregados = 0
    quantPacotesAtuais = 0
    pesoAtualCarregado = 0
    valorCargaTotal = 0

    pesoRestante = pesoMax
    valorRestante = valorSeguroMax
    capacidadeRestante = espacoMax

    loopPrincipal = 0
    while loopPrincipal == 0:
        # MENU...
        _limparTela()

        _titulo('MENU')
        print('\nDia Iniciado! O que deseja fazer?\n')
        _opcoes('1', 'Realizar Parada')
        _opcoes('2', 'Situação Atual')
        _opcoes('3', 'Finalizar Dia')

        _desenhoCaminhao()

        resposta = input(': ')

        if resposta == '1':
            loopResposta = 't'
            while loopResposta == 't':
                _limparTela()

                _titulo('REALIZANDO PARADA')
                print('\nO que deseja fazer?\n')
                _opcoes('1', 'Inserir Pacote')
                _opcoes('2', 'Retirar Pacote')
                _opcoes('3', 'Encerrar Parada')
                    
                resposta = input(': ')
                if resposta == '1':
                    _limparTela()
                    _inserirPacote()
                
                elif resposta == '2':
                    _limparTela()
                    _retirarPacote()

                elif resposta == '3':
                    _limparTela()
                    
                    vtPesoTotalEncerrarParada.extend(vtPesoEncerrarProv)
                    vtPesoEncerrarProv.clear()

                    loopResposta = 'f'

                else:
                    _comandoInvalido()
                    loopResposta = 't'
            
        elif resposta == '2':
            _limparTela()
            _situacaoAtual()

        elif resposta == '3':
            _limparTela()
            _relatorio()
            
            input('\n\nAperte ENTER para fechar o software...')

            _limparTela()
            print('\n\nObrigado por usar meu software! Até breve!\n\n')
            os._exit(os.EX_OK)

        else:
            _comandoInvalido()
            loopPrincipal = 0
