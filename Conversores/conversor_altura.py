def conversor_altura (p):
    centimetro = p*100
    milimetro = p*1000
    return centimetro, milimetro
p= float(input("Me informe a sua altura: "))
c,m = conversor_altura (p)
print(f"A sua altura é {p}, convertida em centimetros fica {c:.1f}, e em milimetros {m}")
