import random

computador = random.randint(0, 10)
tentativas = 0

print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")

while True:
    jogador = int(input("Em que número eu pensei? "))
    tentativas += 1

    if jogador == computador:
        print(f"Você acertou!!! foram necessárias {tentativas} tentativas. ")
        break
    else:
        print(" Tente Novamente! ")
