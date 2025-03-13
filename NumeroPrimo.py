primo = int(input(" digite um número: "))

if primo > 1:
    é_primo = True
    for i in range(2, primo):
        if primo % i == 0:
            é_primo = False
            break
    if é_primo:
        print(f"Sim, {primo} é um número primo.")
    else:
        print(f"Não, {primo} não é um número primo.")
else:
    print("Número inválido. Números primos são maiores que 1.")
