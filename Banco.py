cores = {"vermelho": "\033[1;31;40m]", "verde": "\033[1;32;40m]"}

saldo = 100

print(" para depositar dinheiro a conta, digite 1: ")
print(" para sacar dinheiro da conta, digite 2: ")
print(" para verificar o saldo da conta, digite 3: ")

op = int(input(" qual operação quer verificar? "))

if op == 1:
    valor = float(input(" insira o valor do depósito: "))
    print(cores["verde"], f"seu saldo atual é de {saldo + valor}")
elif op == 2:
    saque = float(input(" qual valor gostaria de sacar? "))
    if saque > saldo:
        print(cores["vermelho"], " dinheiro insuficiente ")
    print(cores["vermelho"], f" seu saldo atual é de {saldo - saque}")
else:
    print(f" seu saldo atual é de: {saldo}")
