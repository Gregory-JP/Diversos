import time
import random
import string

print('-' * 20)

nome = input('Olá, qual seu nome? ')
print('Muito prazer em te conhecer {}, vamos jogar o "Jogo do Adivinha"?'.format(nome))

a = list(string.ascii_lowercase)

while True:
    
    close = input('{}, pressione "Enter" para prosseguir, '
                  'digite \'sair\'para finalizar o jogo \n'
                  'ou digite \'player\' para mudar o nome: '.format(nome))

    print('-' * 80)

    if close == 'sair':
        break
    if close == 'player':
        nome = input('Digite o novo nome: ')
        print('Muito prazer {}!!'.format(nome))

    print('Vou pensar em um número de 0 a 10, tente adivinhar, você só tem 4 tentativas!')

    n = int(random.randint(0, 10))

    p = int(input('Digite um número: '))

    if p > 10:
        print('Apenas números até 10, maiores são inválidos e você perde uma tentativa.')

    elif p in a:
        print('Digite apenas números, por favor!')

    else:
        print('PROCESSANDO...')
        time.sleep(1.5)

    if p == n:
        print('Muito bem. {} foi o número que eu pensei, você ganhou!'.format(n))

    else:
        print('-' * 80)
        p = int(input('Tente outra vez: '))
        
        if p > 10:
            print('Apenas números até 10, maiores são inválidos e você perde uma tentativa.')
        
        else:
            print('PROCESSANDO...')
            time.sleep(1.5)

        if p == n:
            print('Muito bem. {} foi o número que eu pensei, você ganhou!'.format(n))
        
        else:
            print('-' * 80)
            p = int(input('Terceira tentativa, pense bem: '))
            
            if p > 10:
                print('{}, já lhe disse que são números até 10.'.format(nome))
            
            else:
                print('PROCESSANDO...')
                time.sleep(1.5)

            if p == n:
                print('Muito bem. {} foi o número que eu pensei, você ganhou!'.format(n))
            
            else:
                print('-' * 80)
                p = int(input('Última chance, não desista: '))
                
                if p > 10:
                    print('Você desperdiçou sua última chance.')
                
                else:
                    print('PROCESSANDO...')
                    time.sleep(1.5)

                if p == n:
                    print('Muito bem. {} foi o número que eu pensei, você ganhou!'.format(n))
               
                else:
                    print('Eu ganhei, {} foi o número em que eu pensei, foi bom jogar com você {}!'.format(n, nome))

    i = input('Você quer jogar comigo? Dessa vez você pensa em um número,\n'
              'se você aceitar digite \'sim\' ou digite \'sair\' para finalizar o jogo: ')

    if i == 'sair':
        break

    if i == 'sim':

        py_guess = []

        print('Que bom que você aceitou jogar comigo, vamos lá {}!'.format(nome))

        print('Pense em um número de 0 10, mas não me diga qual é, OK?\n'
              'Vou tentar adivinhar, tenho apenas 4 tentativas.')

        print('-' * 80)
        py1 = random.randint(0, 10)
        
        py_guess.append(py1)

        print('PENSANDO...')
        time.sleep(2.5)
        print('Meu primeiro palpite é {}, estou certo?'.format(py1))

        r = input('Se eu acertei digite \'sim\', se eu errei digite \'nao\': ')

        if r == 'sim':
            print('Muito bem, ganhei. {} foi o número que nós pensamos!!'.format(py1))
        
        else:
            print('-' * 80)
            py2 = random.randint(0, 10)

            while py2 in py_guess:
                py2 = random.randint(0, 10)
            
            py_guess.append(py2)

            print('PENSANDO...')
            time.sleep(1.5)
            print('Vou tentar novamente, eis meu segundo chute, número {}. Acertei?'.format(py2))
            
            r = input('Se eu acertei digite \'sim\', se eu errei digite \'nao\': ')

            if r == 'sim':
                print('Muito bem, ganhei. Pensamos no mesmo número, o {}!!'.format(py2))
            
            else:
                print('-' * 80)
                py3 = random.randint(0, 10)

                while py3 in py_guess:
                    py3 = random.randint(0, 10)

                py_guess.append(py3)
                
                print('PENSANDO...')
                time.sleep(1.5)
                print('Penúltima chance, talvez o número {}?'.format(py3))
                
                r = input('Se eu acertei digite \'sim\', se eu errei digite \'nao\': ')

                if r == 'sim':
                    print('Muito bem, ganhei. Pensamos no mesmo número!!')
                
                else:
                    print('-' * 80)
                    py4 = random.randint(0, 10)

                    while py4 in py_guess:
                        py4 = random.randint(0, 10)

                    py_guess.append(py4)

                    print('PENSANDO...')
                    time.sleep(1.5)
                    print('Última chance, vamos lá. Acho que é o número {}'.format(py4))
                    
                    r = input('Se eu acertei digite \'sim\', se eu errei digite \'nao\': ')

                    if r == 'sim':
                        print('Eba!! Ganhei, pensamos igual, no número {}!!'.format(py4))

                    else:
                        print('Muito bem, você venceu! Perdi o "Jogo do Adivinha"')
                        
                        x = int(input('Em qual número você pensou?'))

                        if x > 10:
                            print('Mas isso não vale, eram números de 0 a 10 apenas!!!')

                        elif x == py1 or x == py2 or x == py3 or x == py4:
                            print('Mas eu falei o número {} e você disse que não era, isso não vale, é contra as regras!'.format(x))
                        else:
                          print('Quase chutei o número {}!!Essa foi por pouco...'.format(x))


print('Foi muito bom jogar com você {}!! Volte sempre que desejar.'.format(nome))
print('Convide seus amigos para jogar comigo também, tenho certeza que eles irão gostar!')