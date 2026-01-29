participantes = {}
nomes = set()
idades = set()

for _ in range(2):
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))

    participantes[nome] = idade
    nomes.add(nome)
    idades.add(idade)

print(f"Nomes dos participantes: {', '.join(nomes)}")
print(f"Idades dos participantes: {idades}")
print(f"Participantes e suas idades: {participantes}")

