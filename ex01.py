
convidados = set() 
#conjunto que não aceita valores duplicados
  
while True: 
    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ") 

    if nome.lower() == "sair": 
    #lower() transforma tudo em minúsculo
        break 

    convidados.add(nome) 
    #add insere os convidados no conjunto

print(f"Convidados confirmados: {', '.join(convidados)}") 
#join junta os nomes dos convidados em uma única string separada por vírgulas