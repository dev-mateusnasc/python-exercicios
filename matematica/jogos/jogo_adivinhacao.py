import random
def gerar_numero():
    return random.randint(0,10)
def pedir_tentativa():
    return int(input("Adivinhe o número (0 a 10): "))
def jogo_adivinhacao():
    senha = gerar_numero()
    tentativa = None
    while tentativa != senha:
        tentativa = pedir_tentativa()
        if tentativa != senha:
            print("Número errado, tente novamente: ")
        else:
            print("Você acertou, parabéns!")
jogo_adivinhacao()
