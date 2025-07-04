from collections import deque
#ja vi isso na faculdade 5mil vezes, mas sempre é gostosinho fazer de novo

tarefas = deque()

tarefas.append("Enviar relatório")
tarefas.append("Ligar para Cliente")
tarefas.append("Meeting Noturno")

tarefas.appendleft("Prioridade urgente")

print("Tarefas pendentes:")
for tarefa in tarefas:
    print("-", tarefa)

tarefa_executada = tarefas.popleft()
print("\nExecutando:", tarefa_executada)

tarefa_finalizada = tarefas.pop()
print("Finalizando:", tarefa_finalizada)

tarefas.insert(1, "Checar e-mails")

tarefas.rotate(1)

print(list(tarefas))

tarefas.rotate(-2)
print("\nTarefas após rotacionar para a esquerda:")
print(list(tarefas))

tarefas.append("Enviar relatório")
print("\nOcorrências de 'Enviar relatório':", tarefas.count("Enviar relatório"))

tarefas.remove("Enviar relatório")

print("\nTarefas após remoção:")
print(list(tarefas))
print("\nTotal de tarefas:", len(tarefas))
tarefas.clear()
print("Tarefas após limpar:", list(tarefas))