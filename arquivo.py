""" importa o módulo datetime no início do seu código """
from datetime import datetime
import time  # importa o módulo time para a contagem regressiva
import json


""" Carrega os dados do arquivo JSON no início do programa """
def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar os dados do arquivo JSON.")
        return []
    

""" Salva os dados em um arquivo JSON """
def salvar_dados(visitantes):
    try:
        with open('dados.json', 'w') as arquivo:
            json.dump(visitantes, arquivo, indent=4)
        print("Dados salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")


""" dados iniciais """
visitantes = carregar_dados()


""" Função para exibir o menu """
def exibir_menu():
    print("Selecione uma opção:")
    print("1 - Registrar novo visitante")
    print("2 - Pesquisar visitante")
    print("0 - Salvar e encerrar")


""" função para realizar a contagem regressiva de emergência """
def contagem_regressiva():
    print()
    print("ATENÇÃO: EMERGÊNCIA DETECTADA!")
    print()
    for i in range(10, -1, -1):
        print(f"Tempo restante: {i} segundos")
        time.sleep(1)  # contagem de 1 segundo
    print()
    print("PORTAS TRANCADAS!")
    print()

    """ perguntas de emergência """
    ligar_para_policia = input("Deseja acionar a polícia? (S/N)").upper()
    if ligar_para_policia == "S":
        endereco = input("Digite o endereço do local com CEP: ")
        ocorrido = input("Descreva o ocorrido: ")
        
        """ mostrar informações coletadas """
        print("\nInformações da emergência:")
        print(f"Endereço com CEP: {endereco}")
        print(f"Descrição do ocorrido: {ocorrido}")
        
        """ confirmar informações """
        confirmacao = input("Confirma as informações? (S/N)").upper()
        if confirmacao == "S":
            print("Informações confirmadas.")
            print()
            print("Polícia a caminho!")
            print()
            voltar_ao_menu = input("Voltar ao menu? (S/N)").upper()
            if voltar_ao_menu == "S":
                main()  # Chama a função main() para voltar ao menu
            else:
                print("Programa encerrado.")
        else:
            print("Informações não confirmadas. Refazendo perguntas de emergência.")
            contagem_regressiva()  # refazer as perguntas de emergência

""" função para registrar um novo visitante """
def registrar_visitante():
    while True:
        nome = input("Digite o nome completo do visitante: ")
        if not nome.replace(" ", "").isalpha():
            print("O nome deve conter apenas letras. Tente novamente.")
            continue

        idade = input("Digite a idade do visitante: ")
        try:
            idade = int(idade)
        except ValueError:
            print("A idade deve ser um número inteiro. Tente novamente.")
            continue

        documento = input("Digite o número do CPF de identificação do visitante: ")
        if len(documento) != 11 or not documento.isdigit():
            print("O número do CPF de identificação deve conter 11 dígitos numéricos. Tente novamente.")
            continue

        motivo = input("Digite o motivo da visita: ")

        while True:
            horario_entrada = input("Digite o horário de entrada do visitante (formato HH:MM): ")
            horario_saida = input("Digite o horário de saída do visitante (formato HH:MM): ")
            try:
                entrada = horario_entrada
                saida = horario_saida
                if entrada <= saida:
                    break
                else:
                    print("A hora de saída deve ser maior ou igual à hora de entrada. Tente novamente.")
            except ValueError:
                print("Formato de hora inválido. Use HH:MM. Tente novamente.")
                continue

        visitante = {
            'Nome': nome,
            'Idade': idade,
            'Documento': documento,
            'Motivo': motivo,
            'Entrada': entrada,
            'Saída': saida
        }

        visitantes.append(visitante)

        print("Registro concluído com sucesso.")

        while True:
            continuar = input("Deseja registrar outro visitante? (S/N)").upper()
            if continuar == "S":
                break
            elif continuar == "N":
                return
            else:
                print("Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")

""" Função para pesquisar visitantes com o mesmo nome """
def pesquisar_visitante():
    nome_pesquisa = input("Digite o nome do visitante que deseja pesquisar: ")
    encontrados = []
    for visitante in visitantes:
        if visitante['Nome'] == nome_pesquisa:
            encontrados.append(visitante)

    if encontrados:
        print("Informações dos visitantes com o mesmo nome:")
        for visitante in encontrados:
            print(f"Nome: {visitante['Nome']}")
            print(f"Idade: {visitante['Idade']}")
            print(f"Documento: {visitante['Documento']}")
            print(f"Motivo da visita: {visitante['Motivo']}")
            print(f"Horário de entrada: {visitante['Entrada']}")
            print(f"Horário de saída: {visitante['Saída']}")
            print("-" * 20)
    else:
        print("Visitante não encontrado.")


""" Função principal do menu """
def main():
    while True:
        exibir_menu()
        opcao = input("O que deseja escolher: ")
        if opcao == "1":
            registrar_visitante()
        elif opcao == "2":
            pesquisar_visitante()
        elif opcao == "3":
            salvar_dados(visitantes)
            print("Encerrando o programa.")
            break
        elif opcao == "0":
            salvar_dados(visitantes)
            break
        else:
            print("Opção inválida. Tente novamente.")

""" Iniciar o programa """
if __name__ == "__main__":
    try:
        tem_emergencia = input("Tem alguma emergência? (S/N)").upper()
        if tem_emergencia == "S":
            contagem_regressiva()
        else:
            main()  # Executa o menu de cadastro normalmente
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")