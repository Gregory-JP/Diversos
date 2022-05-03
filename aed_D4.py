import datetime

escolha_mes = int(input('Informe o mês: '))
escolha_ano = int(input('Informe o ano: '))
dias_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']


def mesList(m):
    mList = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']

    return mList[m - 1]


def diasList(d):
    mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return mdays[d - 1]


def calendar(mes, ano):
    # Defini variáveis para valores dentro de minhas listas com base em dados de entrada para ano e mês

    mes_x = mesList(mes)
    num_dias = diasList(mes)
    # Aqui pega a data inicial
    dia_um = datetime.date(ano, mes, 1)
    dia_inicial = dia_um.isoweekday()
    # Imprime mês e ano; O mês é exibido com as primeiras letras, para exibir tudo é só remover [:3] do print abaixo
    print(mes_x[:3], ano)
    # Exibe mês e ano
    print(' '.join(['{0:<2}'.format(w) for w in dias_semana]))
    # Imprime um espaço em branco entre as variáveis
    print('{0:>4}'.format('') * dia_inicial, end='')
    # Verifica se meu dia de início começar no domingo
    if dia_inicial >= 7:
        print()
        dia_inicial = 0
    # Repete o numero de dias do mês, pelo dia 1
    for dias in range(1, num_dias + 1):
        # Print each day
        print('{0:>3}'.format(dias), end=' ')
        # Contador
        dia_inicial += 1
        if dia_inicial >= 7:
            # Caso seja domingo, inicia nova linha
            print()
            # Zera contador
            dia_inicial = 0
    print()


calendar(escolha_mes, escolha_ano)
