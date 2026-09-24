"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
print ("Bem-vindo a consulta de salario!")
salario = float(input("Digite o salario do colaborador da escola"))
if 0<= salario <=400:
    reajuste1=salario*0.15
    salario_reajuste1 = salario+reajuste1
    print(f"Seu salario é de {salario_reajuste1}R$ e o reajuste foi de {reajuste1}R$")
elif 400< salario <=800:
    reajuste2=salario*0.12
    salario_reajuste2= salario+reajuste2
    print(f"Seu salario é de {salario_reajuste2}R$ e o reajuste foi de {reajuste2}R$")
elif 800< salario <=1200:
    reajuste3=salario*0.10
    salario_reajuste3= salario+reajuste3
    print(f"Seu salario é de {salario_reajuste3}R$ e o reajuste foi de {reajuste3}R$")
elif 1200< salario <=2000:
    reajuste4=salario*0.07
    salario_reajuste4= salario+reajuste4
    print (f"Seu salario é de {salario_reajuste4}R$ e o reajuste foi de {reajuste4}R$")
elif salario >2000:
    reajuste5=salario*0.04
    salario_reajuste5= salario+reajuste5
    print (f"Seu salario é de {salario_reajuste5}R$ e o reajuste foi de {reajuste5}R$")


