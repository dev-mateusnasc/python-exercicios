def conversor_dolar(real):
    dolar = real/5.24
    return dolar
real= float(input("Me informe o seu saldo em reais para gerar uma conversão para o dolar: "))
vd = conversor_dolar(real)
print(f"O saldo seu em reais é R${real}, convertido para o dolar ficara: USD{vd:.2f}")
