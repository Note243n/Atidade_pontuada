import os
os.system('clear') # LIMPANDO O TERMINAL 

# SOLICITANDO DADOS 

operacao = input("Informe a operação (+, -, *, /): ")

A = int (input("Informe o valor de A: "))
B = int (input("Informe o valor de B: "))

# IMPRIMINDO RESULTADO 

if operacao == "+":
    resultado = A + B
elif operacao == "-":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    if B != 0:
        resultado = A / B
    else:
        print("Erro: Divisão por zero!")
        exit()
else:
    print("Erro: Operação inválida!")
    exit()

print(f"O resultado da operação é: {resultado}")

# FIM DO PROGRAMA