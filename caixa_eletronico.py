print('Notas disponíveis: R$50.00 - R$20.00 - R$10.00 - R$1.00')

valor = float(input('Qual valor você quer sacar? '))

total = valor
cedula = 50
total_ced = 0

while True:
    if total >= cedula:
        total -= cedula
        total_ced +=1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${cedula}.')
        
        if cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10
        
        elif cedula == 10:
            cedula = 1
        
        total_ced = 0
        
        if total == 0:
            break