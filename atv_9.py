def calcular_reajuste(valor, salario_minimo):
    if valor < (3 * salario_minimo):
        return valor * 1.50
    elif valor < (10 * salario_minimo):
        return valor * 1.20
    elif valor < (20 * salario_minimo):
        return valor * 1.15
    else:
        return valor * 1.10


def main():
    salario_minimo = 1412.00
    numero_funcionarios = 584

    for i in range(numero_funcionarios):
        salario = float(input(f"Insira o salário do funcionário {i + 1} para reajuste: "))
        salario_reajustado = calcular_reajuste(salario, salario_minimo)
        print(f"O valor reajustado é de: R$ {salario_reajustado:.2f}")


main()
