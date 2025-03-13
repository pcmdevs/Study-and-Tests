salario = float(input("Qual é o seu salário? "))

if salario > 1250.00:
    aumento = salario * 0.10
    print(f" o aumento do seu salário é de: R${aumento}")
    total = salario + aumento
    print(f"salário total: R${total}")
else:
    aumento = salario * 0.15
    print(f" o aumento do seu salário é de: R${aumento}")
    total = salario + aumento
    print(f"salário total: R${total}")
