# Calcule quantos azulejos são necessários para azulejar uma parede. É necessário
# conhecer a altura da parede (AP), a sua largura (LP), e a altura do azulejo (A) e sua largura (LA).
# Leia os dados através do teclado.


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
