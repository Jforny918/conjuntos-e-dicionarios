
palavras_em_comum = set()

texto1 = input ("Texto 1: ")

texto2 = input ("texto 2: ")

conjunto1 = set(texto1.split())
conjunto2 = set(texto2.split())
#split() divide o texto em palavras e set() cria um conjunto com essas palavras

palavras_em_comum = conjunto1.intersection(conjunto2)
#intersection() encontra as palavras que estão em ambos os conjuntos

print(f"Palavras em comum: {', '.join(palavras_em_comum)}")
#join() junta as palavras em comum em uma única string separada por vírgulas