"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
soma=0
positivos=0
for i in range(6):
    valor=float(input("Digite o numero: "))

    if valor > 0:
        soma = soma + valor
        positivos = positivos + 1

media = soma / positivos
print(f"A quantidade de numeros positivos é {positivos} e a média final é {media : .1f}")