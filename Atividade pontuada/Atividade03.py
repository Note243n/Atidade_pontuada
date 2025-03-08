import os
os.system('clear') # LIMPANDO O TERMINAL

# SOLICITANDO DADOS 

a = int (input('Informe um valor: '))
b = int (input('Informe o segundo valor: '))
s = a + b
m = a * b

# IMPRIMINDO RESULTADO 

if a == b :
    print(f'O valor {a} e o valor {b} são iguais portanto eles passaram a ser somados dando um resultado de {s} ')
else :
    print(f'O valor {a} e o valor {b} são diferentes portanto eles passaram a ser multiplicados dando um resultado de {m} ')

# FIM DO PROGRAMA