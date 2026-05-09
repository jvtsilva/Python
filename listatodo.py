tarefas = []

while True:
    print("\n--- Lista de Tarefas ---")
    print("1. Mostrar tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        if tarefas:
            print("\nSuas tarefas:")
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
        else:
            print("\nNenhuma tarefa ainda.")
    
    elif escolha == "2":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    
    elif escolha == "3":
        if tarefas:
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
            num = int(input("Número da tarefa para remover: "))
            if 0 < num <= len(tarefas):
                tarefas.pop(num - 1)
                print("Tarefa removida!")
            else:
                print("Número inválido.")
        else:
            print("Nenhuma tarefa para remover.")
    
    elif escolha == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")
