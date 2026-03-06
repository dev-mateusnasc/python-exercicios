def pedir_numero():
    return int(input("Me informe um número para analisar e informar se é impar ou par: "))
def verificar_par_impar():
    if valor % 2 == 0:
        return "par"
    else:
        return "impar"
valor  = pedir_numero()
outro = verificar_par_impar()
print(f"O número informado é {valor}, {outro}")

# Variação do exercicio com sistema de loop(finaliza quando o usuário digita 0)
# def pedir_numero():
#     return int(input("Me informe um número para analisar e informar se é impar ou par: "))
# def verificar_par_impar():
#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "impar"
# numero  = pedir_numero()
# while numero != 0:
#     resultado = verificar_par_impar()
#     print(f"O número informado {numero}, é {resultado}")
#     numero = pedir_numero()
# print("Programa encerrado")
