produtos = {}

for _ in range(3):
    nome = input("Informe o nome do produto: ").strip()
    quantidade = int(input("Informe a quantidade do produto: "))

    produtos[nome] = quantidade

soma = sum(produtos.values())

print(f"Produtos cadastrados: {produtos}")
print(f"A quantidade total de produtos é: {soma}")

alterar = input("Deseja alterar o produto? (s/n): ").lower()

if alterar == 's':
    produto_alterar = input("Informe o produto que deseja alterar: ")
    if produto_alterar in produtos:
        nova_quantidade = int(input("Informe a nova quantidade: "))
        produtos[produto_alterar] = nova_quantidade

        soma_atualizada = sum(produtos.values())
        print(f"Produtos atualizados: {produtos}")
        print(f"A quantidade total de produtos atualizada é: {soma_atualizada}")
    else:
        print(f"O produto {produto_alterar} não está na lista de produtos.")

