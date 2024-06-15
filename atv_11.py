# Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda.
# Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado
# pelo usuário.


def calcular_venda(preco_custo, percentual_acrescimo):
    acrescimo = preco_custo * (percentual_acrescimo / 100)

    valor_venda = preco_custo + acrescimo
    return valor_venda


preco_custo = float(input("Insira o preço de custo do produto: "))
percentual_acrescimo = float(input("Insira o percentual de acréscimo: "))

valor_venda = calcular_venda(preco_custo, percentual_acrescimo)

print(f"O valor de venda do produto é: {valor_venda:.2f}")
