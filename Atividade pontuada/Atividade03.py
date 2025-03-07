import os
os.system('clear')

v1 = int(input('Informe um valor: '))
v2 = int(input('Informe outro valor: '))
s = v1 + v2
m = v1 * v2

if v1 == v2:
    print(f'Os valores {v1} e {v2} são iguai portanto eles foram somados o resultado foi \n > {s} ')
else :
    print(f'Os valores {v1} e {v2} foram diferentes portanto foram multiplicados o resultado foi \n > {m}')