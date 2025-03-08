import os
os.system('clear') # LIMPANDO O TERMINAL

# SOLICITANDO DADOS 

a = int(input('Informe um valor: '))
os.system('clear')

b = int(input('Informe o segundo valor: '))
os.system('clear')

s = a + b
m = a * b

# IMPRIMINDO RESULTADO 

if a == b :
    print(f'\nO valor {a} e o valor {b} são iguais portanto eles passaram a ser somados dando um resultado de\n > {s} \n')
else :
    print(f'O valor {a} e o valor {b} são diferentes portanto eles passaram a ser multiplicados dando um resultado de\n > {m} \n ')

# FIM DO PROGRAMA