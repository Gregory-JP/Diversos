from datetime import date
atual = date.today().year

criancas = 0
adultos = 0
idosos = 0

pessoas = 0

for n in range(0,5):
    pessoas += 1
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nascimento
    if idade < 18:
        criancas += 1
        print('Você ainda não tem 18 anos. Sua idade é {}.'.format(idade))
    elif idade >= 65:
        idosos+= 1
        print('Você já é idoso. Sua idade é de {}.'.format(idade))
    else:
        adultos+= 1
        print('Você já é adulto. Sua idade é {}.'.format(idade))

print('Tivemos {} crianças, {} idosos e {} adultos.'.format(criancas, idosos, adultos))

