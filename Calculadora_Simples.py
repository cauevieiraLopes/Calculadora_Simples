condicao = False
while not condicao:
    print("Qual operação matemática gostaria de realizar?")
    print("[1]Somar\n[2]Subtrair\n[3]Dividir\n[4]Multiplicar\n[5]Potência\n[6]Sair\n")
    operacao = int(input("Digite a operação desejada: "))

    if operacao == 6:
        condicao = True

    elif operacao > 5 or operacao <= 0:
        condicao = False

    elif operacao == 1:
        num1 = float(input("Qual o primeiro valor?"))
        num2 = float(input("Qual o segundo valor?"))
        resultado = num1 + num2
        print(f"A soma de {num1} + {num2} é igual a: {resultado}")

    elif operacao == 2:
        num1 = float(input("Qual o primeiro valor?"))
        num2 = float(input("Qual o segundo valor?"))
        resultado = num1 - num2
        print(f"A subtração de {num1} - {num2} é igual a: {resultado}")

    elif operacao == 3:
        num1 = float(input("Qual o primeiro valor?"))
        num2 = float(input("Qual o segundo valor?"))
        resultado = num1 / num2
        print(f"A divisão de {num1} / {num2} é igual a: {resultado}")

    elif operacao == 4:
        num1 = float(input("Qual o primeiro valor?"))
        num2 = float(input("Qual o segundo valor?"))
        resultado = num1 * num2
        print(f"A multiplicação de {num1} * {num2} é igual a: {resultado}")

    elif operacao == 5:
        num1 = float(input("Qual o primeiro valor?"))
        num2 = float(input("Qual o segundo valor?"))
        resultado = num1 ** num2
        print(f"A potência de {num1} ^ {num2} é igual a: {resultado}")

print("O programa foi encerrado, muito obrigado!")

