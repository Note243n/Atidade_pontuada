import os
os.system('clear')

kmo = int(input('Informe quantos Kg de Morango você deseja levar: '))
km = int(input('Informe quantos Kg de Maça você deseja levar: '))


if kmo <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20
print(f'Quantidade total a ser paga é de {kmo}')
    

if km <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_compra = preco_maca + preco_morango
if total_compra > 50 or kmo + km > 8:
   total_compra *= 0.9


print(f'O valor a ser pago é de R${total_compra:.2f} ')
print(f'Quantidade de morangos em Kg {kmo}')
print(f'Quantidade de maças em Kg {km}')







