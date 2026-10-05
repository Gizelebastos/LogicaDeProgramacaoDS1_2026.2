"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
numero = int(input("Digite um numero inteiro com base na sua impolgação: "))
palavra = "nat"
for i in range (numero):
    palavra += "a"
print (f"tenha um otimo fim de ano e um feliz {palavra}l!!")