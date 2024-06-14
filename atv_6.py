tam = int(input("Digite a quantidade de numeros: "))
num = []

for i in range(tam):
    num.append(int(input(f"Digite o {i + 1}º número: ")))

print("lista a ser ordenada", num)
num.sort()
print("Lista em ordem crescente", num)
