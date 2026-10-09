def calculadora():
    numero1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite + para soma,* para multiplicação, / para divisão ou - para subtração: ")
    numero2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return
    elif operacao == "-":
        resultado = numero1 - numero2
    else:
        print("Operação inválida.")
        return

    print(f"Resultado: {resultado}")


calculadora()
