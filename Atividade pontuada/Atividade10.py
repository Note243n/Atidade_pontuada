import os 
os.system('clear') # LIMPANDO O TERMINAL 

# SOLICITANDO DADOS 

tipo_combustivel = str(input('Informe o tipo de gasolina que deseja: (A | álcool, G | gasolina) \n > ')).upper()

litros_combustivel = float(input('\nInforme a quantidade de litros que deseja comprar: '))

preco_alcool = 3.79
preco_gasolina = 6.59

# IMPRIMINDO RESULTADO 

if tipo_combustivel == 'A':
    if litros_combustivel <= 25:
        desconto = litros_combustivel * preco_alcool * 0.02
        valor_pagar = litros_combustivel * preco_alcool - desconto
        print(f'\nVocê solicitou álcool e um desconto de 2% foi aplicado a sua compra. O valor a ser pago é R${valor_pagar:.2f}\n')

    elif litros_combustivel > 25:
        desconto = litros_combustivel * preco_alcool * 0.04
        valor_pagar = litros_combustivel * preco_alcool - desconto
        print(f'\nVocê solicitou álcool e um desconto de 4% foi aplicado a sua compra. O valor a ser pago é R${valor_pagar:.2f}\n')

elif tipo_combustivel == 'G':
    if litros_combustivel <= 25:
        desconto = litros_combustivel * preco_gasolina * 0.03
        valor_pagar = litros_combustivel * preco_gasolina - desconto
        print(f'\nVocê solicitou gasolina e um desconto de 3% foi aplicado a sua compra. O valor a ser pago é R${valor_pagar:.2f}\n')

    elif litros_combustivel > 25:
        desconto = litros_combustivel * preco_gasolina * 0.05
        valor_pagar = litros_combustivel * preco_gasolina - desconto
        print(f'Você solicitou gasolina e um desconto de 5% foi aplicado a sua compra. O valor a ser pago é R${valor_pagar:.2f}\n')
else:
     print('\nTipo de combustível inválido.\n')
     exit()

# FIM DO PROGRAMA
