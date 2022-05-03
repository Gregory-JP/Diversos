cad_jogador = dict()
gols_marcados = list()
time = list()
while True:

    cad_jogador['Nome'] = str(input('Nome do jogador: '))
    cad_jogador['Partidas'] = int(input(f'Quantas partidas {cad_jogador["Nome"]} jogou? '))

    for p in range(1, cad_jogador["Partidas"] + 1):
        gols = int(input(f'Quantas gols na partida {p}? '))
        gols_marcados.append(gols)

    cad_jogador['Gols'] = gols_marcados[:]
    cad_jogador['Total de Gols'] = sum(gols_marcados)
    gols_marcados.clear()
    time.append(cad_jogador.copy())

    parar = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
    if parar == 'N':
        break
print('-' * 64)

print(f'Cod. ',end='')
for i in cad_jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-' * 64)

for k, v in enumerate(time):
    print(f'{k:>3}  ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

while True:
    opcao = int(input('Qual jogador você deseja ver informações? (999 para parar) '))
    if opcao == 999:
        break
    if opcao >= len(time):
        print(f'ERRO! Não existe jogador com o código digitado({opcao}).')
    else:
        print(f' Dados do Jogador {time[opcao]["Nome"]}')
        for i, g in enumerate(time[opcao]['Gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 64)
