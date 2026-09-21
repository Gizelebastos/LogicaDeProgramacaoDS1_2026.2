#TODO: Implemente a expressão de validação
media_aluno = float(input("Digite a média do aluno"))
frequencia_percentual = float(input("Digite a frequencia do aluno"))

# Crie a variável aprovado com a expressão lógica
aprovado = media_aluno>=6 and frequencia_percentual>=75
print("Status de aprovação:", aprovado)