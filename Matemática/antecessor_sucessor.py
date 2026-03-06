def analisar_numero(n1):
    antecessor = n1 - 1
    sucessor = n1 + 1
    return antecessor, sucessor
n1 = int(input("Digite um número e informarei o sucessor e o antecessor dele: "))
a,s = analisar_numero (n1)
print(f"O número informado foi {n1}, o antecessor é {a}, e o sucessor é {s}!")
