numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 == numero2 == numero3:
    print("Os valores são todos iguais.")
elif numero1 == numero2 and numero1 > numero3:
    print("Os números 1 e 2 são maiores que o número 3.")
elif numero1 == numero3 and numero1 > numero2:
    print("Os números 1 e 3 são maiores que o número 2.")
elif numero2 == numero3 and numero2 > numero1:
    print("Os números 2 e 3 são maiores que o número 1.")
else:
    maximo = max(numero1, numero2, numero3)
    if maximo == numero1:
        print("O primeiro número é o maior.")
    elif maximo == numero2:
        print("O segundo número é o maior.")
    else:
        print("O terceiro número é o maior.")




