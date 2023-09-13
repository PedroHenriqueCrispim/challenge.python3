# Dados iniciais
visitantes = []

# Função para exibir o menu
def exibir_menu():
    print("Selecione uma opção:")
    print("1 - Registrar novo visitante")
    print("2 - Pesquisar visitante")
    print("0 - Encerrar programa")

# Função para registrar um novo visitante
def registrar_visitante():
    while True:
        nome = input("Digite o nome completo do visitante: ")
        if not nome.replace(" ", "").isalpha():
            print("O nome deve conter apenas letras. Tente novamente.")
            continue

        idade = input("Digite a idade do visitante: ")

        documento = input("Digite o número do CPF de identificação do visitante: ")
        if len(documento) != 11 or not documento.isdigit():
            print("O número do CPF de identificação deve conter 11 dígitos numéricos. Tente novamente.")
            continue

        motivo = input("Digite o motivo da visita: ")
        horario_entrada = input("Digite o horário de entrada do visitante (formato HH:MM): ")
        horario_saida = input("Digite o horário de saída do visitante (formato HH:MM): ")

        visitante = {
            'Nome': nome,
            'Idade': idade,
            'Documento': documento,
            'Motivo': motivo,
            'Entrada': horario_entrada,
            'Saída': horario_saida
        }

        visitantes.append(visitante)

        print("Registro concluído com sucesso.")

        continuar = input("Deseja registrar outro visitante? (S/N)")
        if continuar.upper() != "S":
            break

# Função para pesquisar um visitante
def pesquisar_visitante():
    nome_pesquisa = input("Digite o nome do visitante que deseja pesquisar: ")
    encontrado = False
    for visitante in visitantes:
        if visitante['Nome'] == nome_pesquisa:
            print(f"Nome: {visitante['Nome']}")
            print(f"Idade: {visitante['Idade']}")
            print(f"Documento: {visitante['Documento']}")
            print(f"Motivo da visita: {visitante['Motivo']}")
            print(f"Horário de entrada: {visitante['Entrada']}")
            print(f"Horário de saída: {visitante['Saída']}")
            encontrado = True
            break

    if not encontrado:
        print("Visitante não encontrado.")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("O que deseja escolher: ")
        if opcao == "1":
            registrar_visitante()
        elif opcao == "2":
            pesquisar_visitante()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")

# Iniciar o programa
if __name__ == "__main__":
    main()
