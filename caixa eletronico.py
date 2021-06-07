print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)

valor = int(input("quanto quer sacar? R$"))
total = valor
cedula = 200
estoque = 15
quantidade = 0

while True:
    if total >= cedula and estoque > 0:
        total -= cedula
        quantidade += 1
        estoque -= 1
    else:
        if quantidade > 0:
            print(f'Total de {quantidade} cédulas de R${cedula}')
        if cedula == 200:
            cedula = 100
            estoque = 10
        elif cedula == 100:
            cedula = 50
            estoque = 20
        elif cedula == 50:
            cedula = 20
            estoque = 12
        elif cedula == 20:
            cedula = 10
            estoque = 30
        elif cedula == 10:
            cedula = 5
            estoque = 50
        elif cedula == 5:
            cedula = 2
            estoque = 60
        if cedula == 2:
            cedula = 1
            estoque = 15
        quantidade = 0
        if total == 0:
            break
