"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distância_percorrida = float(input("digite a distância percorrida no total"))
total_de_combustível = float(input("digite o total de combustível gasto"))
consumo_médio = ((distância_percorrida + total_de_combustível)/2)
print(f"O consumo médio foi{consumo_médio:.2f}Km/L")
