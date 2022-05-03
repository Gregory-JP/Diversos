import datetime

atual = datetime.date.today().year

genero = input('Qual seu gênero, para masculino digite 1 e para feminino digite 2: ')

if genero == '2':
    print('Seu alistamento não é obrigatório.')

else:
    print('Seu alistamento é obrigatório pois você é do sexo masculino.')

ano = int(input('Digite o seu ano de nascimento: '))

idade = atual - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if idade == 18:
    print('Você deve se alistar esse ano!')

elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para você se alistar.'.format(saldo))
    alistamento = atual + saldo
    print('Seu alistamento será em {}.'.format(alistamento))

elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos atrás.'.format(saldo))
    alistamento2 = atual - saldo
    print('Seu alistamento foi em {}.'.format(alistamento2))
