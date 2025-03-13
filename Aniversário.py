maiores_de_idade = 0
menores_de_idade = 0

for i in range(1, 8):
    data = int(input(f" Qual o ano do seu nascimento {i}? "))
    resultado = 2025 - data
    if resultado >= 18:
        maiores_de_idade += 1
    elif resultado < 18:
        menores_de_idade += 1

print(f" Total de maiores de idade: {maiores_de_idade} ")
print(f" Total de menores de idade: {menores_de_idade} ")
