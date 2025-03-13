soma = 0

for i in range(1, 7):
    n = int(input(f" digite o valor {i}: "))
    if n % 2 == 0:
        soma += n
print(f" a soma dos números pares é {soma}")
