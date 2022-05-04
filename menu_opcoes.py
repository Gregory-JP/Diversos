n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

while True:

    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair
    ''')

    e = int(input('O que você deseja fazer? '))

    if e == 1:
        soma = n1 + n2
        print('A soma é {}.'.format(soma))
    elif e == 2:
        multi = n1 * n2
        print('A multiplicação é {}.'.format(multi))
    elif e == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        else:
            print('O maior número é {}.'.format(n2))
    elif e == 4:
        n1 = int(input('Digite outro valor: '))
        n2 = int(input('Digite o outro valor: '))
    elif e == 5:
        break
    else:
        print('Opção Inválida.')

print('Obrigado por usar o nosso sistema!')
