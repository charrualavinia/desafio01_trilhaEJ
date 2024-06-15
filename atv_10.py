# Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que
# a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da
# variável A. Apresentar os valores trocados.


def troca_valores(A, B):
    A, B = B, A
    return A, B


A = input("Digite o valor de A: ")
B = input("Digite o valor de B: ")

A, B = troca_valores(A, B)

print(f"Após a troca, o valor de A é: {A}")
print(f"Após a troca, o valor de B é: {B}")
