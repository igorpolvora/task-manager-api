import requests

url = "https://jsonplaceholder.typicode.com/todos"

#GET
def consultar_tarefas():
    try:
        usuario_id = int(input("Digite o ID do usuário: "))
        print("Consultando tarefas...")
        print()

        if usuario_id <=0:
            print("O ID deve ser positivo.")
            return

    except ValueError:
            print("Por favor, digite um número válido")
            return

    try:
        parametros = {
            "userId": usuario_id
        }
    
        response = requests.get(
            url, 
            params=parametros,
            timeout=10
        )

        response.raise_for_status()
    
    except requests.RequestException as e:
        print(f"Error fetching API data: {e}")
        return 

    try:
        dados = response.json()

    except requests.exceptions.JSONDecodeError:
        print("A API retornou uma resposta inválida.")
        return
    
    if not dados:
        print("Nennhuma tarfa encontrada para este usuáriio.")
        return

    
    tarefas_total = len(dados)
    tarefas_concluidas = 0
    
    for tarefa in dados:
        status = "Concluída" if tarefa["completed"] else "Pendente"

        print(f"ID: {tarefa['id']}")
        print(f"Title: {tarefa['title']}")
        print(f"Status: {status}")
        print()

        if tarefa["completed"]:
            tarefas_concluidas += 1

    tarefas_pendentes = tarefas_total - tarefas_concluidas

  
    print("Resumo das Tarefas do usuário: ", usuario_id)
    print("Total de tarefas:", tarefas_total)
    print("Total de tarefas concluídas:", tarefas_concluidas)
    print("Total de tarefas pendentes:", tarefas_pendentes)
    print("\n")

#POST
def criar_tarefa():


    print("Criando tarefas...")
    try:
        usuario_id = int(input("Digite o ID do usuário responsável: "))
        
        if usuario_id <= 0:
            print("O ID do usuário deve ser um número positivo.")
            return

        titulo = input("Digite o título da nova tarefa: ").strip()

        if not titulo:
            print("O título da tarefa não pode estar vazio.")
            return

        nova_tarefa = {
            "userId": usuario_id,
            "title": titulo,
            "completed": False
        }

    except ValueError:
        print("Por favor, digite um número válido.")
        return

    try:
        response = requests.post(
            url,
            json=nova_tarefa,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Erro ao criar tarefa: {e}")
        return

    print("Status HTTP:", response.status_code)
    print("Resposta:", response.json())

#PUT
def substituir_tarefa():
    print("Substituindo tarefa...")

    try:
        tarefa_id = int(input("Digite o ID da tarefa: "))

        usuario_id = int(input("Digite o ID do usuário responsável: "))

        titulo = input("Digite o novo título da tarefa: ").strip()

        if tarefa_id <= 0 or usuario_id <= 0:
            print("Os IDs devem ser positivos.")
            return

        if not titulo:
            print("O título não pode estar vazio.")
            return

        url = f"https://jsonplaceholder.typicode.com/todos/{tarefa_id}"


        tarefa_atualizada = {
            "userId": usuario_id,
            "title": titulo,
            "completed": True  
        }

    except ValueError:
        print("Por favor, digite um número válido.")
        return

    try:
        response = requests.put(
            url,
            json=tarefa_atualizada,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Erro ao atualizar a tarefa: {e}")
        return
    
    print("Status HTTP:", response.status_code)
    print("Resposta:", response.json())

#PATCH
def atualizar_status():
    print("Atualizando status...")

    try:
        tarefa_id = int(input("Digite o ID da tarefa que deseja atualizar: "))

        if tarefa_id <= 0:
            print("O ID da tarefa deve ser um número positivo.")
            return

        url = f"https://jsonplaceholder.typicode.com/todos/{tarefa_id}"

        atualizacao = {
            "completed": True
        }

    except ValueError:
                print("Por favor, digite um número válido.")
                return

    try:
        response = requests.patch(
            url,
            json=atualizacao,
            timeout=10
        )

        response.raise_for_status()

    
    except requests.RequestException as e:
        print(f"Erro ao atualizar a tarefa: {e}")
        return

    print("Status HTTP:", response.status_code)
    print("Resposta:", response.json())

#SUBMENU
def atualizar_tarefa():
        print("Atualizando tarefas...")
        
        while True:
            print("===== ATUALIZAR TAREFA =====\n")

            print("1 - Substituir tarefa (PUT)")
            print("2 - Atualizar status (PATCH)")
            print("0 - Voltar ao menu principal")

            try:
                print("\n")
                opcao = int(input("Escolha uma opção: "))

                if opcao == 1:
                    substituir_tarefa()
                elif opcao == 2:
                    atualizar_status()
                elif opcao == 0:
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Escolha entre 0 e 2.")

            except ValueError:
                    print("Por favor, digite um número válido.")

#DELETE
def excluir_tarefa():
    print("Excluindo tarefas...")

    try:
        tarefa_id = int(input("Digite o ID da tarefa que deseja excluir: "))

        if tarefa_id <= 0:
            print("O ID da tarefa deve ser positivo.")
            return

        url = f"https://jsonplaceholder.typicode.com/todos/{tarefa_id}"

    except ValueError:
        print("Por favor, digite um número válido.")
        return

    try:
        response = requests.delete(
            url,
            timeout=10
        )

        response.raise_for_status()

        print(f"Tarefa {tarefa_id} excluída com sucesso!")

    except requests.exceptions.HTTPError as e:
        print(f"Falha ao excluir a tarefa. Erro HTTP: {e}")
        return
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição ao excluir a tarefa: {e}")
        return


    print("Status HTTP:", response.status_code)

while True:
    print("===== GERENCIADOR DE TAREFAS =====\n")

    print("1 - Consultar tarefas")
    print("2 - Criar tarefa")
    print("3 - Atualizar tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

    
    try:
        print("\n")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            consultar_tarefas()
        elif opcao == 2:
            criar_tarefa()
        elif opcao == 3:
            atualizar_tarefa()
        elif opcao == 4:
            excluir_tarefa()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha entre 0 e 4.")

    except ValueError:
        print("Por favor, digite um número válido.")