import os 
os.system('clear') # LIMPANDO O TERMINAL

# SOLICITANDO DADOS

a = int(input('Digite o primeiro valor: '))
os.system('clear')

b = int(input('Digite o segundo valor: '))
os.system('clear')

c = int(input('Digite o terceiro valor: '))
os.system('clear')

s = a + b

# IMPRIMINDO RESULTADO

if s > c :
    print(f' A soma dos números {a} + {b} é maior que {c}\n')

elif s == c :
    print(f'A soma dos números {a} + {b} é igual a {c} \n')

else:
    print(f' A soma dos números {a} + {b} é menor que {c}\n')

# FIM DO PROGRAMA
