pali = input("Digite uma palavra ou frase: ")

pali = ''.join(e for e in pali if e.isalnum()).lower()

if pali == pali[::-1]:
    print("Sim, essa palavra ou frase é um palíndromo.")
else:
    print("Não, essa palavra ou frase não é um palíndromo.")
