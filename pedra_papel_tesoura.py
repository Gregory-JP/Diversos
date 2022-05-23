from random import randint
from time import sleep

escolhas = ('Pedra', 'Tesoura', 'Papel')

computador = randint(0,2)

print('''Suas opções são:
[ 0 ] Pedra
[ 1 ] Tesoura
[ 2 ] Papel''')

jogador = int(input('Qual a sua jogada? '))

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ...')
sleep(1)

print('-=' * 14)

print('O computador escolheu {}.'.format(escolhas[computador]))
print('O jogador escolheu {}.'.format(escolhas[jogador]))

print('-=' * 14)

if computador == 0:

    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('Computador ganhou!')

    elif jogador == 2:
        print('Jogador ganhou!')

    else:
        print('Jogada Inválida')

elif computador == 1:

    if jogador == 1:
        print('EMPATE!')

    elif jogador == 0:
        print('Jogador ganhou!')

    elif jogador == 2:
        print('Computador ganhou!')

    else:
        print('Jogada Inválida!')

elif computador == 2:

    if jogador == 2:
        print('EMPATE!')

    elif jogador == 1:
        print('Jogador ganhou!')

    elif jogador == 0:
        print('Computador ganhou!')

    else:
        print('Jogada Inválida!')
