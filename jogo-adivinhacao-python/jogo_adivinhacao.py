import random

def jogar():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print("🎮 Jogo de Adivinhação")
    print("🤔 Tente adivinhar o número entre 1 e 10")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"✅ Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("🔼 O número é maior.")
        else:
            print("🔽 O número é menor.")
jogar()
jogar_novamente = input("Quer jogar novamente? (s/n) ")
if jogar_novamente.lower() == 's':
    jogar()