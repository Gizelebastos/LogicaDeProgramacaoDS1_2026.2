"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("Bem-vindo ao nosso programa!")
ano_de_nascimento = int(input("digite a ano de nascimento: "))
idade_em_2026 = (2026 - ano_de_nascimento)
print(f"a idade que a pessoa completara ate final de 2026 é de {idade_em_2026} anos")