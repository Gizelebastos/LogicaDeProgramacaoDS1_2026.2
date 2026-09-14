
## 🛠️ Prática do Aluno (Mão na Massa)
#Agora é a sua vez! Crie 4 variáveis para cadastrar um novo produto no estoque de informática da escola:
#1. `nome_produto` (texto)
#2. `quantidade_estoque` (inteiro)
#3. `preco_unitario` (ponto flutuante)
4. `disponivel_para_venda` (booleano)

#Em seguida, exiba o valor de cada uma e seu respectivo tipo usando `print()` e `type()`.

nome_do_produto = str("digite o nome do seu produto")
quantidade_estoque = int(input("digite a quantidade em estoque"))
preco_unitario = float(input("digite o preco unitario"))
disponível_para_venda = bool (input("Está disponivel para venda"))

print(type(nome_do_produto))
print(type(quantidade_estoque))
print(type(preco_unitario))
print(type("diponível_para_venda"))