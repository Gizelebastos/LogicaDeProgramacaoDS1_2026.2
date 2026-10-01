# TODO: Desenvolva o acumulador com parada no 0
soma = 0
numero = int (input("Digite um numero inteiro: "))
while numero != 0:
    soma= soma + numero
    print ("Errado! Por favor, digite um numero inteiro diferente: ")
    numero = int(input("digite um numero inteiro: "))
print (f"O resultado é {soma} !")
