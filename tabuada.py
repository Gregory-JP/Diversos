while True:
    num = int(input('Digite um número para ver sua tabuada [0 para sair]: '))
    if num == 0:
        print('Volte sempre!')
        break
    else:
        for n in range(1,11):
            print('{} x {} = {}'.format(num, n, num * n))
