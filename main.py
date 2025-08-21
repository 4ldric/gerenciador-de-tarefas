# Funções
tarefas = []
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!!!")
    return

def visualizar_tarefa(tarefas):
    print("\n== Lista de Tarefas ==")
    for indice, tarefa in enumerate(tarefas, start = 1):
        status = "✓" if tarefa["concluida"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f'{indice}. [{status}] {nome_tarefa}')
    return

def editar_tarefa(tarefas,indice_tarefa):
    indice_tarefa -= 1
    novo_nome = input("Atualize a tarefa: ")
    tarefas[indice_tarefa]["tarefa"] = novo_nome
    print("Tarefa atualizada com sucesso!!!")

def concluir_tarefa(tarefas, indice_tarefa):
    indice_tarefa -= 1

    if  tarefas[indice_tarefa]["concluida"]:
        tarefas[indice_tarefa]["concluida"] = False
    else: 
        tarefas[indice_tarefa]["concluida"] = True


# Menu de Comandos
while True:
    print("\n== Menu Do Gerenciador ==")
    print(
"""
[1]. adicionar tarefa
[2]. ver tarefas
[3]. editar tarefa
[4]. concluir/remover tarefa
[5]. excluir tarefas concluidas
[6]. Sair 
"""
    )
    digito = int(input("Digite uma opção: "))

    if digito == 1:
        tarefa = input("Adicione uma tarefa: ")
        adicionar_tarefa(tarefas, tarefa)
    elif digito == 2:
        visualizar_tarefa(tarefas)
    elif digito == 3:
        visualizar_tarefa(tarefas)
        indice_tarefa = int(input("\nInforme a tarefa que deseja editar: "))
        editar_tarefa(tarefas, indice_tarefa)
    elif digito == 4:
        visualizar_tarefa(tarefas)
        indice_tarefa = int(input("\nInforme a tarefa: "))
        concluir_tarefa(tarefas,indice_tarefa)
    elif digito == 5:
        pass
    elif digito == 6:
        print("encerrando....")
        break
    else:
        print("Informe um digito valido!")
        print("Retornando ao menu...")
