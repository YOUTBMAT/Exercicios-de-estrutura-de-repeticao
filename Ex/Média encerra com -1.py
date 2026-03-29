soma = 0
quantidade = 0

while True:
    numero = float(input("Digite um número (-1 para encerrar): "))
    if numero == -1:
        break
    soma += numero
    quantidade += 1

if quantidade > 0:
    media = soma/quantidade
    print(f"Média dos números: {media:.2f}")
else:
    print ("Nenhum númeor foi digitadox")