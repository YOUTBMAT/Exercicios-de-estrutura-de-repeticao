nota = int(input("Digite sua nota: "))
if 10>=nota>=0:
    valida=True
else:
    valida=False
while valida ==False:
    print("Nota invalida")
    nota = int(input("Digite sua nota: "))
    if 10>=nota>=0:
      valida=True
if valida==True:
    print("Sua nota é",nota)