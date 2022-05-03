from datetime import date
dados = dict()

dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (digite 0 caso não possua): '))
if dados['CTPS'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}.')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-'* 30)

for k, v in dados.items():
    print(f'{k} tem o valor {v}.')
print('-' * 30)
