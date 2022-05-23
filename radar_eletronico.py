v = float(input('Qual é a velocidade? '))

i = float(v) - 80

m = float(i) * 7

if v <= 80:
    print('Dirija com segurança, faça uma boa viagem e tenha uma chegada segura!')
else:
    print('Você foi multado em R$ {:.2f} por estar acima do limite permitido, reduza a velocidade!'.format(m))

#color