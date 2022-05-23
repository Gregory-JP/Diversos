palavras = ('mercado', 'carro', 'programador', 'garrafa', 'filme', 'celular', 'computador', 'musica', 'videos', 'trabalho',
            'alma', 'mestre', 'luta', 'karate', 'vida', 'virtude', 'coragem')
for p in palavras:
    print(f'\nNa palavra {p} temos as seguintes vogais: ', end='')
    for letra in p:
        if letra.lower() in 'a e i o u':
            print(letra, end=' ')

# é possível adicionar vogais com acento, "a à á ã e é ê..."
