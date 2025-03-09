import os
os.system('clear') # LIMPANDO O TERMINAL 

# SOLICITANDO DADOS 

nome_produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02

elif quantidade <= 10:
    desconto = total * 0.03

else:
    desconto = total * 0.05

total_pagar = total - desconto



# IMPRIMINDO RESULTADO 

print(f"Descrição do produto: {nome_produto}")
print(f"Quantidade adquirida: {quantidade}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Total: R${total:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${total_pagar:.2f}")

# FIM DO PROGRAMA