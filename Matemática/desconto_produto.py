def desconto_valor(preco):
    multi = preco * 5
    divi = multi/100
    p3= preco - divi
    return p3
preco=float(input("Informe o número que irei analisar e aplicar 5% de desconto: "))
resultado = desconto_valor(preco)
print (f"O valor do item é de R${preco}, com desconto ficara: R${resultado}")
