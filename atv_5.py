def palindromo():
    string = input("Digite uma string: ").strip()

    string_normalizada = string.replace(" ", "").lower()

    if string_normalizada == string_normalizada[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


palindromo()
