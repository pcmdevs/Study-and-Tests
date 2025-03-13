import random
import string


def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + \
        string.punctuation.replace(',', '.').replace(
            '~', '´').replace('+', '?')
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


minimo_caracteres = 4
while True:
    tamanho_senha = int(
        input(f"Digite o tamanho da senha (mínimo de {minimo_caracteres} caracteres): "))
    if tamanho_senha >= minimo_caracteres:
        break
    else:
        print("Tamanho da senha inválido. Por favor, digite um valor maior ou igual ao mínimo.")

senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada:", senha_gerada)
