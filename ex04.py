permissoes_principais = set()
while True:
    principais = input("Permissões principais ('0' para finalizar): ")
    if principais == '0':
        break
    permissoes_principais.update(principais.split(", "))

permissoes_solicitadas = set()
while True:
    solicitadas = input("Permissões solicitadas ('0' para finalizar): ")
    if solicitadas == '0':
        break
    permissoes_solicitadas.update(solicitadas.split(", "))

verificar_permissoes = permissoes_principais.intersection(permissoes_solicitadas)

if verificar_permissoes == set():
    print("As permissões solicitadas NÃO fazem parte das permissões principais.")
else:
    print(f"Permissões em comum: {', '.join(verificar_permissoes)}")
    print("As permissões solicitadas fazem parte das permissões principais.")
    
