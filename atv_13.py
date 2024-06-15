# Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante
# o semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado
# (media maior ou igual 7), Reprovado (media <= 5) e Recuperação (média entre 5.1 a 6.9).


def calcular_media(notas):
    return sum(notas) / len(notas)


def calculo_mencao(media):
    if media >= 7:
        return "Aprovado"
    elif media <= 5:
        return "Reprovado"
    else:
        return "Recuperação"


nome = input("Digite o nome do aluno: ")
notas = []
for i in range(1, 4):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

media = calcular_media(notas)

mencao = calculo_mencao(media)

print(f"Nome: {nome}")
print(f"Média: {media:.2f}")
print(f"Menção: {mencao}")
