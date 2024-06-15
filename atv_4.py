# Crie um algoritmo que peça ao usuário que informe 10 números inteiros e armazene-os
#  em um vetor. A seguir, apresente a multiplicação de todos os elementos pares e a soma de
#  todos os elementos ímpares.


def calc(multi_pares=1, soma_impares=0):  # elementos neutros da multi e soma
    vetor = []

    for i in range(10):
        num = int(input(f"Insira o {i + 1} número inteiro: "))
        vetor.append(num)

    for num in vetor:
        if num % 2 == 0:
            multi_pares *= num
        else:
            soma_impares += num

    print(f"Multiplicação de todos os elementos pares: {multi_pares}")
    print(f"Soma de todos os elementos ímpares: {soma_impares}")

calc()
