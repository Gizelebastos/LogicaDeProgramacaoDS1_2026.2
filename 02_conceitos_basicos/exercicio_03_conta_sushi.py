"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
print(f"Seja bem-vindo! Vamos calcular a conta a pagar!")
valor_da_conta = float(input("digite o valor total da conta (R$)"))
taxa_de_serviço = valor_da_conta * 0.10 
valor_final = valor_da_conta + taxa_de_serviço
print(f"O valor total da sua conta é {valor_final: .2f}!")
