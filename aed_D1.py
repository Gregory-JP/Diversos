lista_1 = []
lista_2 = []

while True:

    num = int(input('Qual valor você deseja adicionar a lista 1? '))
    lista_1.append(num)
    troca = str(input('Deseja mudar para a lista 2? [S/N]: ')).upper().strip()[0]

    if troca == 'S':
        break

print("\033[31mO programa será encerrado assim que a lista 2 estiver com o mesmo"
      "números de elementos da lista 1!\033[m")


while True:

    num = int(input('Qual valor você deseja adicionar a lista 2? '))
    lista_2.append(num)
    if len(lista_1) == len(lista_2):
        break

print(lista_1)
print(lista_2)
print('-' * 30)


def soma(lista1, lista2):
    n = 0
    for numeros in lista1:
        s = lista1[n] + lista2[n]
        print(f'{lista1[n]} + {lista2[n]} = {s}')
        n+=1
    print('-' * 30)


def diferenca(lista1, lista2):
    n = 0
    for numeros in lista1:
        sub = lista1[n] - lista2[n]
        print(f'{lista1[n]} - {lista2[n]} = {sub}')
        n += 1
    print('-' * 30)


def produto(lista1, lista2):
    n = 0
    soma_produto = 0
    for numeros in lista1:
        prod = lista1[n] * lista2[n]
        print(f'{lista1[n]} * {lista2[n]} = {prod}')
        soma_produto += prod
        n += 1
    print(f'A soma dos produtos é igual a {soma_produto}.')


soma(lista_1, lista_2)
diferenca(lista_1, lista_2)
produto(lista_1, lista_2)
