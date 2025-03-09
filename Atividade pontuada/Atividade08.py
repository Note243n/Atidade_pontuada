import os
os.system('clear') # LIMPANDO O TERMINAL 


tabela_precos = {
    "VERDE": 10,
    "AZUL": 20,
    "AMARELO": 30,
    "VERMELHO": 40
}

# SOLICITANDO DADOS 

cor = input("Digite a cor do CD: ").upper().strip()

# IMPRIMINDO RESULTADO 

if cor in tabela_precos:
    print(f"\nO preço do CD {cor} é ${tabela_precos[cor]}\n")

else:
    print("\nCor não encontrada na tabela de preços\n")
    exit()

# FIM DO PROGRAMA