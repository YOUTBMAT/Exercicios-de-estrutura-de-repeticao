while True:
    try:
        conta = int(input('''
1: soma
2: subtração
3: multiplicação
4: divisão
0: sair
Digite o número da opção escolhida: '''))
    except Exception:
        print('''
Número/Caractere inválido''')
        continue
    if conta == 0:
        break

    if conta not in [1,2,3,4]:
        print('''
Número/Caractere inválido''')
        continue
    try:
        n1, n2 = map(int, input("Digite dois números separados por espaço: ").strip().split())

    except ValueError:
        print("Opção digitada é inválida")
        continue

   
    if conta == 1:
        print(f"Resultado: {n1 + n2}")

    elif conta == 2:
        print(f"Resultado: {n1 - n2}")

    elif conta == 3:
        print(f"Resultado: {n1 * n2}")

    elif conta == 4:
        if n2 == 0:
            print("Resultado: indefinido")
            continue
        print(f"Resultado: {n1 / n2}")