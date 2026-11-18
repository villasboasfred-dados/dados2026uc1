# Crie um algoritmo para dizer se uma pessoa é maior de idade ou não.

nome = input("Nome: ")
idade = int(input("Idade: "))

if idade >= 18:
    print("Maior de idade")
    print("Pode tirar careira")
else:
    print("Menor de idade")
    faltam = 18 - idade
    print(f"Faltam {faltam} ano(s) paa completar 18.")

    