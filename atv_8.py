def fatorial(n):
    if n < 0:
        return "Numero invalido"
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


numero = int(input("Digite um número inteiro: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
