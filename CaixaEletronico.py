valores_notas = ["R$1", "R$5", "R$10", "R$50", "R$100"]
print(f"notas disponiveis {valores_notas} ")

saque = int(input("qual o valor do saque? R$ "))

total = saque

if total < 10 or total > 600:
    print("saque inválido. ")


nota = 100

totalnota = 0

while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        print(f"Foi usado um total de {totalnota} notas de R${nota} para realizar o saque. ")
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        totalnota = 0
        if total == 0:
            break
