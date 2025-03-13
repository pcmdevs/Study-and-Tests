print(" os números ímpares múltiplos de 3 entre 1 e 500 são: ")

for i in range(1, 500+1):
    if i % 3 == 0 and i % 2 == 0:
        print("\033[0;32;40m ", i)
