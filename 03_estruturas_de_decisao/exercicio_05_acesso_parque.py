"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
from xml.dom.minidom import ElementInfo

print ("bem-vindo! consulte o valor do seu ingresso")
idade = int (input("Digite a idade do visitante"))
valor = 100
if idade <=12:
    desconto1=valor*0.50
    valor_final=valor-desconto1
    print (f"O seu ingresso é do tipo Infantil, assim o valor final é de {valor_final}")
elif idade >=60:
    desconto2= valor-valor
    valor_final2=desconto2
    print (f"O seu ingresso é do tipo Melhor Idade e o valor é de {valor_final2} com desconto de 100%!!")
elif idade>=13 and idade<=59:
    desconto3=valor
    valor_final3=desconto3
    print (f"O seu ingresso é do tipo Integral, o valor a ser pago é de {valor_final3}")

