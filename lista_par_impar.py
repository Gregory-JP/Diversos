lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista.append(num)
        lista_par.append(num)
    else:
        lista.append(num)
        lista_impar.append(num)
    p = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if p == 'N':
        break
print(f'Você digitou os seguintes números: {lista}')
print(f'Os números pares são: {lista_par}')
print(f'Os números ímpares são: {lista_impar}')
