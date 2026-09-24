"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math
A = float(input("Digite o valor de A"))
B = float(input("Digite o valor de B"))
C = float(input("Digite o valor de C"))
delta=B**2-4*A*C
if delta>=0:
    raizx1=((-B+math.sqrt(delta)/(2*A)))
    raizx2=(-B-math.sqrt(delta)/(2*A))
    print(f"Os valores da raiz são {raizx1 :.2f} e {raizx2 :.2f}")
else:
    print ("Impossivel calcular")
