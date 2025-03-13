distancia = int(input("Qual a distância da viagem em KM? "))

if distancia > 200:
    preço = distancia * 0.45
else:
    preço = distancia * 0.50

print(f"o preço da sua passagem ficou de: R${preço}")
