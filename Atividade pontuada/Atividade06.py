import os
os.system('clear') # LIMPANDO O TERMINAL 

# SOLICITANDO DADOS 

unidade1 = float(input('Digite a nota da primeira unidade: '))

unidade2 = float(input('Digite a nota da segunda unidade: '))

s = unidade1 + unidade2
media = s / 2 

# IMPRIMINDO RESULTADO

if media >= 6 :
    print(f'Parabens você foi aprovado sua média foi de {media} ! ')

elif media < 6 and media > 3:
    print(f'Você está de recuperação sua média foi {media} ! ')
    
elif media <= 3.9 :
    print(f'Você foi reprovado sua média foi  {media} ! ')

# FIM DO PROGRAMA