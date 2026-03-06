def analisar_numero(n1):
    raiz= n1 **(1/2)
    dobro= n1 * 2
    triplo= n1 * 3
    return raiz, dobro, triplo
n1 = int(input("Digite um número para gerar o calculo de raiz quadrada, dobro e triplo do valor informado: "))
r, d, t = analisar_numero(n1)
print(f"O número informado foi: {n1},")
print(f"Em seguida a raiz será {r}, o dobro será {d}, e o triplo ficará {t}")
