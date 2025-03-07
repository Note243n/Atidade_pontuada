import os
os.system('clear')

A = int(input('Digite um numero: '))
B = int(input('Digite um segundo numero: '))
C = int(input('Digite um terceiro numero: '))
s = A + B
os.system('clear')




   

if s > C:
    print(f' O numero {A} + {B} Somados é maior que {C}')

elif s == C:
    print(f'O numero {A} + {B} somados é igual a {C}')

else :
    print(f' O numero {A} + {B} somados é menor que {C}')

print()