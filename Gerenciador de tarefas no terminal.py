# Gerenciador de tarefas pelo terminal
tarefas = [
    {"titulo": "Estudar Python", "concluida": False},
    {"titulo": "Fazer compras", "concluida": True},
]

def menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("0. Sair")

def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\n=== Lista de Tarefas ===")
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i + 1}. {tarefa['titulo']} - status: {status}")

def marcar_tarefa_concluida():
    listar_tarefas()
    if not tarefas:
        return
    indice = ler_numero("Digite o número da tarefa que deseja marcar como concluída: ") - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    indice = ler_numero("Digite o número da tarefa que deseja remover: ") - 1
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida['titulo']}' removida com sucesso!")
    else:
        print("Número de tarefa inválido.")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_tarefa_concluida()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "0":
        print("Agenda fechada...")
        break
    else:
        print("Opção inválida, tente novamente.")
