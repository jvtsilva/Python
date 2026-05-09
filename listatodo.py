# 📝 Lista de Tarefas em Python
# Este programa cria um menu simples para gerenciar tarefas.
# Você pode adicionar, listar e remover tarefas.

# Criamos uma lista vazia para armazenar as tarefas
tarefas = []

# Usamos um loop infinito (while True) para manter o programa rodando
while True:
    # Exibe o menu de opções
    print("\n--- Lista de Tarefas ---")
    print("1. Mostrar tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

    # O usuário escolhe uma opção digitando um número
    escolha = input("Escolha uma opção: ")

    # Se a escolha for "1", mostramos todas as tarefas
    if escolha == "1":
        if tarefas:  # Verifica se a lista não está vazia
            print("\nSuas tarefas:")
            # enumerate gera índice e valor (ex.: 1. Comprar pão)
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
        else:
            print("\nNenhuma tarefa ainda.")
    
    # Se a escolha for "2", adicionamos uma nova tarefa
    elif escolha == "2":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)  # Adiciona à lista
        print("Tarefa adicionada!")
    
    # Se a escolha for "3", removemos uma tarefa
    elif escolha == "3":
        if tarefas:
            # Mostra as tarefas com número
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
            # Usuário escolhe qual remover
            num = int(input("Número da tarefa para remover: "))
            if 0 < num <= len(tarefas):
                tarefas.pop(num - 1)  # Remove pelo índice
                print("Tarefa removida!")
            else:
                print("Número inválido.")
        else:
            print("Nenhuma tarefa para remover.")
    
    # Se a escolha for "4", encerramos o programa
    elif escolha == "4":
        print("Saindo...")
        break  # Encerra o loop
    
    # Caso o usuário digite algo inválido
    else:
        print("Opção inválida.")
