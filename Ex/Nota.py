nota = int(input("Digite sua nota: "))
if 10>nota>=0:
    valida=True
else:
    valida=False
while nota ==False:
    print("Nota invalida")
    nota = int(input("Digite sua nota: "))
if valida==True:
    print("Sua nota é",nota)