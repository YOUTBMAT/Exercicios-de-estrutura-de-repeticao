loop = 10

quantPar = 0
quantImp = 0
par = []
impar = []
while True:
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        quantPar = quantPar + 1
        par.append(numero)
    else:
        quantImp = quantImp + 1
        impar.append(numero)

    loop = loop -1
    if loop == 0:
        break
print (quantPar,"números são par, a lista de números pares é",par)
print (quantImp,"números são ímpar, a lista de números ímpares é",impar)