vogais = set("aeiou")
string = input("Digite uma string: ").strip().lower()

contador = 0
for i in string:
    if i in vogais:
        contador += 1

print(f"Número de vogais na string: {contador}")
