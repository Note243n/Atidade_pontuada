import os 
os.system('clear') # LIMPANDO O TERMINAL 

# VARIÁVEIS

preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

# SOLICITANDO DADOS 

quantidade_morango = float(input('Informe a quantidade de morangos (em kg): '))

quantidade_maca = float(input('Informe a quantidade de maçãs (em kg): '))

# IMPRIMINDO RESULTADO

if quantidade_morango <= 5:
   preco_morango = quantidade_morango * preco_morango_ate_5kg

else:
    preco_morango = quantidade_morango * preco_morango_acima_5kg

if quantidade_maca <= 5:
    preco_maca = quantidade_maca * preco_maca_ate_5kg
else:
    preco_maca = quantidade_maca * preco_maca_acima_5kg

total_compra = preco_morango + preco_maca

if quantidade_morango + quantidade_maca >= 10 or total_compra >= 15:
    total_compra *= 0.9


print(f'O total da compra é R${total_compra:.2f}')

# FIM DO PROGRAMA

