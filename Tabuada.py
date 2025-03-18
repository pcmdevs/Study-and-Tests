numero = int(input(" Digite o número que queira saber a tabuada: "))

def tabuada(multi):
    for multi in range(0, 11):
        print(f"a tabuada do número {numero} é: {numero} x {multi}", numero * multi)

tabuada(numero)
    
    
    