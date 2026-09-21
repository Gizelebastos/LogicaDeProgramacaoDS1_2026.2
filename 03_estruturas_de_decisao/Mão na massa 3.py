# TODO: Implemente o menu utilizando match-case ou elif

#Opção 1: Consultar livro
# Opção 2: Realizar empréstimo
#Opção 3: Devolver livro
#Qualquer outra opção: Mensagem de "Opção Não Encontrada".


# Desenvolva a estrutura de seleção aqui
print ("Bem-vindo a nossa biblioteca!")
opcao = int(input("escolha a opcao desejada: 1-consultar, 2-emprestimo, 3-devolver :"))

if opcao ==1:
        print ("Consultar um livro.")
elif opcao==2:
        print ("Realizar um emprestimo")
elif opcao==3:
        print ("Devolver um livro")
else:
    print ("opcao nao encontrada")

