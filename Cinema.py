# Fazer uma função que reserva assentos de cinema, a função deve retornar uma lista de dicionários de todas as cadeiras indicando
# se estão ou não reservadas e o seu número. Depois de reservado a lista deve retornar com todas as cadeiras após as reservas.

assentos_disponiveis = ["A1", "A3", "A5", "B2", "B3", "B5", "C1", "C3", "C4"]
assentos_reservados = ["A2", "A4", "B1", "B4", "C2", "C5"]


def reservar_assento():
    print(" Os assentos diponíveis são: ", assentos_disponiveis)
    print(" Os assentos reservados são: ", assentos_reservados)
    while True:
        reserva = input(" Qual assento gostaria de reservar? ").upper()
        if reserva in assentos_disponiveis:
            assentos_disponiveis.remove(reserva)
            assentos_reservados.append(reserva)
            break
        else:
            print(" Assento já reservado, tente outro. ")

    print(" Imprimindo ingresso... ")

    print(" Assentos reservados ", assentos_reservados)

    print(" Reserva feita com sucesso! ")


reservar_assento()
