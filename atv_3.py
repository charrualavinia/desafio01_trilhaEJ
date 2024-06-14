def calcular_desconto(total, quantidade):
    if quantidade <= 5:
        desconto = total * 0.02
    elif quantidade <= 10:
        desconto = total * 0.03
    else:
        desconto = total * 0.05
    return desconto


def calculo_valor():
    nome = input("Insira a descriçao do produto: ")
    quantidade = int(input("Insira a quantidade desejada: "))
    valor = float(input("Insira o valor unitário: "))

    total = valor * quantidade
    print(f"O valor total do produto {nome} é: {total}")

    desconto = calcular_desconto(total, quantidade)
    print(
        f"O valor do desconto é de {desconto} ({desconto / total * 100:.2f}%), e o total a pagar é: {total - desconto}")


calculo_valor()
