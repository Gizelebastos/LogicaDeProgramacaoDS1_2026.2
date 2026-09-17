"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
print(f"Bem vindo aos calculos das notas do curso tecnico")
nota_um= int (input("digite a primeira nota"))
nota_dois= int (input("digite a segunda nota"))
nota_tres= int (input("digite a terceira nota"))
nota_um_peso = int (nota_um * 2)
nota_dois_peso = int(nota_dois * 3)
nota_tres_peso= int(nota_tres * 5)
média_final= float ((nota_um_peso + nota_dois_peso + nota_tres_peso)/10)
print (f"a média final do curso tecnico é {média_final : .2f}")