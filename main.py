
# Funções
tarefas = []
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!!!")

















# Menu de 
while True:
    print("\n== Menu Do Gerenciador ==")
    print(
"""
[1]. adicionar tarefa
[2]. ver tarefas
[3]. editar tarefa
[4]. concluir tarefa
[5]. remover tarefa
[6]. Sair 
"""
    )
    digito = int(input("Digite uma opção: "))

    if digito == 1:
        tarefa = input("Adicione uma tarefa: ")
        adicionar_tarefa(tarefas, tarefa)
    elif digito == 2:
        pass
    elif digito == 3:
        pass
    elif digito == 4:
        pass
    elif digito == 5:
        pass
    elif digito == 6:
        print("encerrando....")
        break
    else:
        print("Informe um digito valido!")
        print("Retornando ao menu...")
