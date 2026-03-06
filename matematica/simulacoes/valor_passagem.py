def pedir_distancia():
    return float(input("Me informe a distancia para calcular o valor da passagem: "))
def calculo_distancia():
    if trajeto > 200:
        return trajeto * 0.45
    else:
        return trajeto * 0.50
trajeto = pedir_distancia()
trajeto2= calculo_distancia()
print(f"A distancia da sua passagem é de {trajeto}, a conversão do valor ficara: R${trajeto2}")
