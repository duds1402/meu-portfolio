alunos = []

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = input("Idade do aluno: ")
    matricula = input("Matrícula: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "matricula": matricula
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("\nLista de Alunos:")
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Matrícula: {aluno['matricula']}")
    print()

def buscar_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"Aluno encontrado: {aluno['nome']} | Idade: {aluno['idade']}\n")
            return
    print("Aluno não encontrado.\n")

def remover_aluno():
    matricula = input("Digite a matrícula do aluno a remover: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print("Aluno removido com sucesso.\n")
            return
    print("Aluno não encontrado.\n")

def menu():
    while True:
        print("=== Sistema de Cadastro de Alunos ===")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Buscar aluno")
        print("4. Remover aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
