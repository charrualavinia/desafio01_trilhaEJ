def calculo_azulejos():
    AP = float(input('Digite a altura da parede:'))
    LP = float(input('Digite a largura da parede:'))
    A = float(input('Digite a altura do azulejo:'))
    LA = float(input('Digite a largura do azulejo:'))

    altura = AP / A
    largura = LP / LA

    total = altura * largura

    print(" o total de azulejos eh:", total)

print("-- calculo de azulejos --")
calculo_azulejos()