while True:
    conta = input("Digite a conta (digite 'sair' para parar): ").strip().lower()
    if conta == 'sair': 
        break

    permitidos = "0123456789+-*/(). "

    valido = True
    for caractere in conta:
        if caractere not in permitidos:
            valido = False
            break

    try:
        resultado = eval(conta)
        print (resultado)

    except ZeroDivisionError:
        print("Não é possível dividir com 0")

    except Exception:
        print("Formato digitado inválido")
