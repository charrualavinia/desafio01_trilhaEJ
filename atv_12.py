# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem
# do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o custo de fábrica,
# e depois a percentagem do distribuidor sobre o resultado). Supondo que a percentagem do distribuidor
# seja de 28% e os impostos 45%. Escrever um algoritmo que leia o custo de fábrica de um carro e
# informe o custo ao consumidor do mesmo.


def calcular_custo(custo_fabrica):
    percentual_distribuidor = 28
    percentual_impostos = 45

    valor_impostos = custo_fabrica * (percentual_impostos / 100)

    custo_com_impostos = custo_fabrica + valor_impostos

    valor_distribuidor = custo_com_impostos * (percentual_distribuidor / 100)

    custo_consumidor = custo_com_impostos + valor_distribuidor

    return custo_consumidor


custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

custo_consumidor = calcular_custo(custo_fabrica)

print(f"O custo ao consumidor do carro é: {custo_consumidor:.2f}")
