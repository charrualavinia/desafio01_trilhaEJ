#  Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando
# “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos
# como maior de idade.


def verificar_idade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"


for i in range(1, 76):
    idade = int(input(f"Digite a idade {i}: "))
    resultado = verificar_idade(idade)
    print(f"Pessoa {i} é {resultado}.")
