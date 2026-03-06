def calcular_media(n1, n2 , n3 , n4 , n5):
    soma = n1 + n2 + n3 + n4 + n5
    media= soma / 5
    return media
n1= float(input("Informe a nota em Português: "))
n2= float(input("Informe a nota em Matemática: "))
n3= float(input("Informe a nota em História: "))
n4= float(input("Informe a nota em Fisica: "))
n5= float(input("Informe a nota em Artes: "))
resultado = calcular_media(n1, n2, n3, n4, n5)
if resultado < 6:
    print(f"Sua média foi {resultado}, estude mais!")
else:
    print(f"Sua média foi {resultado}, parabéns!")
