
idades = []

nomes = []

sexos = []

homem_mais_velho = ""

idade_homem_mais_velho = 0

quantas_mulheres_menos_20 = 0

for i in range(1, 5):

    nome = input(f" Qual o seu nome? {i}: ")
    idade = int(input(f" Qual a sua idade? {i}: "))
    sexo = input(f" Qual o seu sexo? {i}: ")
    idades.append(idade)

    nomes.append(nome)
    sexos.append(sexo)

    if sexo.lower() == "masculino" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    if sexo.lower() == "feminino" and idade < 20:
        quantas_mulheres_menos_20 += 1

media_idade = sum(idades) / len(idades)

print(f" A média de idade do grupo é: {media_idade} anos")
print(f" O nome do homem mais velho é: {homem_mais_velho} ")
print(f" Foram cadastradas {quantas_mulheres_menos_20} mulheres abaixo de 20 anos. ")
