# Aplicar um algoritmo que calcule a média das notas bimestrais de uma escola
# (media = (nota1 + nota2 + nota3 + nota4)/4). O algoritmo deve repetir o cálculo até que o
# usuário responda “N” à pergunta “Deseja continuar (S/N) ?”.


def calcular_media():
    nota1 = int(input('Digite a primeira nota: '))
    nota2 = int(input('Digite a segunda nota: '))
    nota3 = int(input('Digite a terceira nota: '))
    nota4 = int(input('Digite a quarta nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("A media eh:", media)


continuar = 'S'

while continuar.upper() != 'N':
    calcular_media()
    continuar = str(input('Quer continuar? [S/N] ')).upper()
