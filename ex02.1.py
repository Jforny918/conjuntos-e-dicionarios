texto1 = set(input("Texto 1: ").lower().split())

texto2 = set(input("Texto 2: ").lower().split())

palavras_em_comum = texto1.intersection(texto2)

print (f"Palavras em comum: {palavras_em_comum}")

