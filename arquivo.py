# Rafael Autieri - RM550885
# Caique Chargas - RM551943
# Rodrigo Resende - RM551057
# Pedro Crispim - RM99005
# Giuliano Romaneto - RM99694

# Esse é um programa python para controlar os visitantes que entram nas escolas/faculdades, aqui você vê o nome da pessoa, a idade, o horario que ela entrou e saiu o numero do documento e o motivo da entrada e depois ainda consegue ver os dados das pessoas antigas que ja foram cadastrada. 

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

        visitante = [nome, idade, documento, motivo, horario_entrada, horario_saida]
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
        if visitante[0] == nome_pesquisa:
            print(f"Nome: {visitante[0]}")
            print(f"Idade: {visitante[1]}")
            print(f"Documento: {visitante[2]}")
            print(f"Motivo da visita: {visitante[3]}")
            print(f"Horário de entrada: {visitante[4]}")
            print(f"Horário de saída: {visitante[5]}")
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
            preencher_dados()
            registrar_visitante()
        elif opcao == "2":
            pesquisar_visitante()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")

# Função auxiliar para preencher os dados
def preencher_dados():
    print("\nPor favor, preencha os dados do visitante.")
    print("O nome deve conter apenas letras.")
    print("O número do documento de identificação deve conter 11 dígitos numéricos.")
    print("Os horários devem estar no formato HH:MM.\n")

# Iniciar o programa
if __name__ == "__main__":
    main()
