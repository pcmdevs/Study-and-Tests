num1 = float(input(" digite o primeiro número: "))
num2 = float(input(" digite o segundo número: "))

print(" qual operação deseja realizar? ")
print(" 1 soma")
print("2 subtração")
print("3 multiplicação")
print("4 divisão")

op = int(input(" digite o número da operação: "))

if op == 1:
    resultado = num1 + num2
elif op == 2:
    resultado = num1 - num2
elif op == 3:
    resultado = num1 * num2
elif op == 4:
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!")
        exit()
else:
    print("Erro: Opção inválida!")
    exit()

print(f"O resultado da sua operação é: {resultado} ")

if op % 2 == 0:
    print("seu número é par")
else:
    print(" seu número é ímpar")

if op >= 0:
    print("seu número é positivo ")
else:
    print("seu número é negativo")

if resultado % 1 == 0:
    print("seu número é inteiro ")
else:
    print("seu número é decimal ")
