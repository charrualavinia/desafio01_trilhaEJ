# Desenvolva um algoritmo que conte quantas vogais existem em uma string fornecida
# pelo usuário.
# Entrada: Uma string.
# Saída: O número de vogais na string.


vogais = set("aeiou")
string = input("Digite uma string: ").strip().lower()

contador = 0
for i in string:
    if i in vogais:
        contador += 1

print(f"Número de vogais na string: {contador}")
