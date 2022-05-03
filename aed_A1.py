km = [22495, 22841, 23185, 23400, 23772, 24055, 24434, 24804, 25276]
consumo = [36.6, 33.9, 31.5, 33.0, 36.6, 44.1, 42.9, 45.6]

cont = len(consumo)
i = 0

print("Os consumos médios foram:")
print('-' * 46)
while cont >= 0:
    x = km[i]
    z = consumo[i]
    i += 1
    y = km[i]
    consumo_medio = (y - x) / z
    print(f'{y} Km - {x} Km / {z:.1f} litros = {consumo_medio:.2f} Km/l')
    cont = cont - 1
    if cont == 0:
        break
print('-' * 46)

cont = len(consumo)
i = 0
abast = 0

print('Os consumos médios cumulativos foram:')

while cont >= 0:
    x = km[0]
    z = consumo[i]
    y = km[i]
    abast = consumo[i] + abast
    i += 1
    cmc = (y - x) / abast
    print(f'{y} Km - {x} Km / {abast:.1f} litros = {cmc:.2f} Km/l')
    cont = cont - 1
    if cont == 0:
        break

print('-' * 46)
