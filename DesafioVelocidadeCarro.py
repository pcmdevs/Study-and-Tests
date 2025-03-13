velocidade = float(input("Qual foi a velocidade do carro? "))

if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f" Você foi multado no valor de: R${multa}")
else:
    print("Você está dentro do limite de velocidade.")
