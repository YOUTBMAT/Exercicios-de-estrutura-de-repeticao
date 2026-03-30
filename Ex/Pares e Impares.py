loop = 10

par = []
impar = []
while True:
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        # numero = par
        par.append(numero)
    else:
        # numero = impar
        impar.append(numero)

    loop = loop -1
    if loop == 0:
        break
print ("A lista de números pares é",par)
print ("A lista de números ímpares é",impar)