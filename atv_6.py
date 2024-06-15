#  Escreva um programa que leia uma lista de números e os ordene em ordem crescente.
# Entrada: Uma lista de números.
# Saída: A lista de números ordenada.


tam = int(input("Digite a quantidade de numeros: "))
num = []

for i in range(tam):
    num.append(int(input(f"Digite o {i + 1}º número: ")))

print("lista a ser ordenada", num)
num.sort()
print("Lista em ordem crescente", num)
