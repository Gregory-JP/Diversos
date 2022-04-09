import time

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO,
[2] converter para OCTAL,
[3] converter para HEXADECIMAL.''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('PROCESSANDO...')
    time.sleep(2)
    print('O número {} convertido para binário é {}.'.format(num, bin(num)))

elif opcao == 2:
    print('PROCESSANDO...')
    time.sleep(2)
    print('O número {} convertido para OCTAL é {}.'.format(num, oct(num)))

elif opcao == 3:
    print('PROCESSANDO...')
    time.sleep(2)
    print('O número {} convertido para HEXADECIMAL é {}.'.format(num, hex(num)))

else:
    print('PROCESSANDO...')
    time.sleep(2)
    print('Opção inválida!')

