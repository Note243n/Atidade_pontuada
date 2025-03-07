import os
os.system('clear')

nome = str(input('Informe o seu nome: '))
sexo = int(input('imforme o seu sexo, 1 para feminino 2 para masculino \n > '))
estadoC = int(input('informe o seu estado civil, 1 para Casado(a) 2 para Solteiro(a) \n > '))

if sexo == 1 and estadoC == 1:
   tempoC = int(input('Informe o tempo de casado(a)'))
   print(f'Seu nome é {nome} \n Seu sexo é {sexo} \n Seu estado civil é {estadoC} \n Seu tempo de casado é {tempoC} ')




