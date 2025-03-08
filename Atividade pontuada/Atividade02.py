import os
os.system('clear') # LIMPANDO O TERMINAL

# SOLICITANDO DADOS

nome = input('Informe seu nome: ').strip()
os.system('clear')

sexo = input('informe seu sexo (MASCULINO/FEMININO): ').strip().upper()

os.system('clear')

estado_civil = input ('Informe seu estado civil: ').strip().upper()

os.system('clear')

# IMPRIMINDO RESULTADO 

if sexo == "FEMININO" and estado_civil == "CASADA"  :
    tempo_casados = input('Digite o tempo de casado(a) (anos): ')
    os.system('clear')

    print('\nDados do usuário:\n')
    print(f'Seu nome é {nome} ')
    print(f'Seu sexo é {sexo} ')
    print(f'Seu  estado civil é {estado_civil}(A)')
    print(f'Seu tempo de casada é {tempo_casados} anos')

elif sexo == 'FEMININO' and estado_civil == 'SOLTEIRO' or 'SOLTEIRA' :
    print('\nDados do usuário:\n')
    print(f'Seu nome é {nome} ')
    print(f'Seu sexo é {sexo} ')
    print(f'Seu  estado civil é {estado_civil}(A)')

elif sexo == 'MASCULINO' and estado_civil == 'CASADO' :
    print('\nDados do usuário:\n')
    print(f'Seu nome é {nome} ')
    print(f'Seu sexo é {sexo} ')
    print(f'Seu  estado civil é {estado_civil}(A)')

elif sexo == 'MASCULINO' and estado_civil == 'SOLTEIRO' :
    print('\nDados do usuário:\n')
    print(f'Seu nome é {nome} ')
    print(f'Seu sexo é {sexo} ')
    print(f'Seu  estado civil é {estado_civil}(A)')

else:
     print('Não há informações adicionais.')

# FIM DO PROGRAMA