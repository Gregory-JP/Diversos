cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'Treze', 'Quatorze', 'Quinze','Dezesseis',
        'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}.')
        i = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if i == 'N':
            break
    else:
        print('Tente novamente!', end=' ')

