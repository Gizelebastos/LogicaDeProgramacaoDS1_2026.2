"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

codigo_do_item = float(input("Digite o codigo do lanche"))
consumida = float (input("Digite a quantidade consumida"))
if codigo_do_item==1:
    preço_total=(consumida)*4
    print(f"O valor a ser pago é de {preço_total}R$")
elif codigo_do_item==2:
    preço_total=(consumida)*4.50
    print(f"O valor a ser pago é de {preço_total}R$")
elif codigo_do_item==3:
    preço_total=(consumida)*5
    print(f"O valor a ser pago é de {preço_total}R$")
elif codigo_do_item==4:
    preço_total=(consumida)*2
    print(f"O valor a ser pago é de {preço_total}R$")
elif codigo_do_item==5:
    preço_total=(consumida)*1.50
    print(f"O valor a ser pago é de {preço_total}R$")