produtos = {}

for p in range(3):
    nome = input (f"Informe o nome do produto: ")
    quantidade = int (input (f"Informe a quantidade do produto: ")) 

    produtos[nome] = quantidade
    soma = sum(produtos.values())

print(f"Produtos cadastrados: {produtos}")
print (f"A quantidade total de produtos é: {soma}")
    