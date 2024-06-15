# Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida
# e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário),
# o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
# Se quantidade <= 5 o desconto será de 2%
# Se quantidade > 5 e quantidade <=10 o desconto será de 3%
#  Se quantidade > 10 o desconto será de 5%


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
