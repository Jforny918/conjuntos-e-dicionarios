
equipe_a = set (input ("Informe as tarefas da equipe A: ").split(", "))
equipe_b = set (input ("Informe as tarefas da equipe B: ").split(", "))

equipes = equipe_a.union(equipe_b)

remover_tarefa = input ("Informe a tarefa que deseja remover: ")

if remover_tarefa in equipes:
    equipes.remove(remover_tarefa)
    print (f"Tarefa '{remover_tarefa}' removida.")
    print ("Tarefas atualizadas: " + ', '.join(equipes))
else:
    print (f"A tarefa {remover_tarefa} não está na lista de tarefas")
