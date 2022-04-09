# lista ordenada sem usar o .sort()

lista = []

for c in range(0,5):
    num = int(input('Digite um valor para adicionar a lista: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                break
            pos+=1
print(f'A sua lista em ordem é {lista}.')