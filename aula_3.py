# Crie um algoritmo para dizer se uma pessoa é maior de idade ou não.

nome = input("Nome: ")
idade = int(input("Idade: "))

if idade >= 18:
    validacao = "Maior de idade"
else:
    validacao = "Menor de idade"

print(f"{nome} é {validacao}")