materias = ["Português", "Matemática", "História"]

notas = {}

nome_aluno = str(input(" Digite o seu nome: ")).capitalize()

for materia in materias:
    while True:
        nota = float(input(f" {nome_aluno}, qual foi a sua nota em {materia}? "))
        if nota < 0 or nota > 10:
            print("Digite uma nota válida, entre 0 e 10. ")
        else:
            notas[materia] = nota
            break

def media(notas_dict): 
    soma_notas = sum(notas_dict.values())
    media_final = soma_notas / 3
    if media_final >= 7:
        print(f" Parabéns {nome_aluno}, sua media final foi de {media_final:.1f} e você foi aprovado. Parabéns!!! ")
    else:
        print(f" Desculpe {nome_aluno}, sua media final foi de {media_final:.1f} e você não foi aprovado. ")

media(notas)