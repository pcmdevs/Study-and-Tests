idades = []
homem_mais_velho = ""
idade_homem_mais_velho = 0
idade_mulheres = []

for i in range(1, 5):
    nome = input(f" Qual o seu nome? {i}: ")
    idade = int(input(" Qual a sua idade?: "))
    sexo = input(" Qual o seu sexo?: ")
    idades.append(idade)

    totalidades = sum(idades)
    media = totalidades / 4

    if sexo.lower() == "m" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if sexo.lower() == "f" and idade < 20:
        idade_mulheres.append(idade)
        total_mulheres = len(idade_mulheres)

print(f" A média de idade das pessoas é de: {media} ")
print(f" O nome do homem mais velho é: {homem_mais_velho}")
print(f" A quantidade de mulheres abaixo de 20 anos é de: {total_mulheres} mulher(es)")
