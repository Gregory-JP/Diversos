"""
frase = input('Digite uma palavra ou frase: ').strip().upper()
palavras = frase.split()
sem_espaco = ''.join(palavras)
inverso = ''

for letra in range(len(sem_espaco) -1, -1, -1):
    inverso += sem_espaco[letra]
print('Você digitou {}, o inverso é {}!'.format(sem_espaco, inverso))

if inverso == sem_espaco:
    print('Temos um palíndromo')
else:
    print('A frase ou palavra digitada não é um palíndromo')
"""

#fazendo sem o uso do "for"

frase_1 = input('Digite uma frase ou palavra: ').strip().upper()
palavras_1 = frase_1.split()
junto = ''.join(palavras_1)

inverso_1 = junto[::-1]
print('Você digitou {}, o inverso é {}!'.format(junto, inverso_1))

if inverso_1 == junto:
    print('Temos um palíndromo!')
else:
    print('Não é palíndromo.')
