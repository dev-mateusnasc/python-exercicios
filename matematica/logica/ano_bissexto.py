def solicitar_informacao():
    return int(input("Me informe um ano: "))
def calculo_do_ano():
    if valor % 400 == 0:
        return "É bissexto"
    elif valor % 4 == 0 and valor % 100 != 0:
        return "É bissexto"
    else:
        return "Não é bissexto"
valor = solicitar_informacao()
resultado = calculo_do_ano()
print(resultado)
