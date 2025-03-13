reta1 = float(input(" comprimento da primeira reta: "))
reta2 = float(input(" comprimento da segunda reta: "))
reta3 = float(input(" comprimento da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(" sim, é possível formar um triângulo. ")
else:
    print(" não, não é possível formar um triângulo. ")
