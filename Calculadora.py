print(" 1 - Soma ")
print(" 2 - subtração ")
print(" 3- divisão ")
print(" 4- multiplicação ")

while True:
    conta = int(input("Qual operação deseja realizar? (1-4): "))
    if conta >= 1 and conta <= 4:
        break
    else:
        print("Erro! Digite um número válido entre 1 e 4.")

primeiro_valor = float(input(" Qual o primeiro valor? "))
segundo_valor = float(input(" Qual o segundo valor? "))


def calculadora(calculo):
    if calculo == 1:
        print(" O resultado da operação é: ", primeiro_valor + segundo_valor)
    elif calculo == 2:
        print(" O resultado da operação é: ", primeiro_valor - segundo_valor)
    elif calculo == 3:
        if segundo_valor == 0:
            print(" Erro, divisão por 0")
        else:
            print(" O resultado da operaçao é: ",
                  primeiro_valor / segundo_valor)
    else:
        print(" O resultado da operação é: ", primeiro_valor * segundo_valor)


calculadora(conta)
