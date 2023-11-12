import time  #importa o módulo time para a contagem regressiva
import json
import requests #importando a API   

""" Carrega os dados do arquivo JSON sobre os visitantes """
def carregar_dados():
    try:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar os dados do arquivo JSON.")
        return []

""" salva os dados no arquivo JSON (dados.json) """
def salvar_dados(visitantes):
    try:
        with open('dados.json', 'w', encoding='utf-8') as arquivo:
            json.dump(visitantes, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

""" dados iniciais """
visitantes = carregar_dados()

""" função para exibir o menu """
def exibir_menu():
    print("Selecione uma opção:")
    print("1 - Registrar novo visitante")
    print("2 - Pesquisar visitante")
    print("3 - Editar visitante")
    print("4 - Salvar visitantes")
    print("0 - Encerrar")

""" carrega os dados do arquivo JSON de ocorrências """
def carregar_dados_ocorrencias():
    try:
        with open('ocorrencias.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar os dados do arquivo JSON.")
        return []

""" salva os dados no arquivo JSON de ocorrências """
def salvar_dados_ocorrencias(ocorrencias):
    try:
        with open('ocorrencias.json', 'w', encoding='utf-8') as arquivo:
            json.dump(ocorrencias, arquivo,ensure_ascii=False, indent=4)
        print("Dados de ocorrências salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados de ocorrências: {e}")

""" dados iniciais das ocorrências """
ocorrencias = carregar_dados_ocorrencias()

""" função para consultar cep usando API """
def consultar_cep(cep):
    while True:
        try:
            url = f'https://opencep.com/v1/{cep}'
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dicionario = resposta.json()
                if 'erro' in dicionario:
                    print("Erro: CEP não existe. ")
                    novo_cep = input("Digite o CEP novamente: ")
                    if novo_cep.isdigit() and len(novo_cep) == 8: #verifica se tem 8 digitos no CEP
                        cep = novo_cep
                    else:
                        print("CEP invalido. Tente novamente. ")
                else:
                    return dicionario
            else:
                continue
        except requests.exceptions.ConnectTimeout:
            print('Erro ao carregar API, aguarde..')
            continue

""" função para realizar a contagem regressiva de emergência """
def contagem_regressiva():
    print()
    print("ATENÇÃO: EMERGÊNCIA DETECTADA!")
    print()
    for i in range(5, -1, -1):
        print(f"Tempo restante: {i} segundos")
        time.sleep(1)  #contagem de 1 segundo
    print()
    print("PORTAS TRANCADAS!")
    print()

    """ perguntas de emergência """
    ligar_para_policia = input("Deseja acionar a polícia? (S/N)").upper()
    if ligar_para_policia == "S":
        cep = input("Informe o CEP: ")
        dicionario = consultar_cep(cep)
        dicionario.pop('ibge')
        endereco = input("Digite o nome da universidade: ")
        ocorrido = input("Descreva o ocorrido:")

        """ mostrar informações coletadas """
        print("\nInformações da emergência:")
        print(f"Nome da universidade: {endereco}")
        print(f"Descrição do ocorrido: {ocorrido}")
        print(f"CEP: {dicionario['cep']}")
        print(f"Rua: {dicionario['logradouro']}")
        print(f"Complemento: {dicionario['complemento']}")
        print(f"Bairro: {dicionario['bairro']}")
        print(f"Cidade: {dicionario['localidade']}")
        print(f"Estado: {dicionario['uf']}")

        informacoes = {
            'Universidade': endereco,
            'Ocorrido': ocorrido,
            'Informações': dicionario
        }

        """ confirmar informações """
        confirmacao = input("Confirma as informações? (S/N)").upper()
        if confirmacao == "S":
            ocorrencias.setdefault('Ocorrencias', []).append(informacoes)  #adiciona as informações de emergência à lista de ocorrências
            salvar_dados_ocorrencias(ocorrencias)
            print("Informações confirmadas.")
            print()
            print("Polícia a caminho!")
            print()
            dicas_de_emergencia = input("Prescione 'S' para ver as dicas de emergencias: ")
            if dicas_de_emergencia == "s":
                print()
                print("Dicas de emergencia:\n")
                print("1-Fique em um local seguro")
                print("2-Silencio absoluto")
                print("3-Bloqueie as portas")
                print("4-Evite ficar perto de portas e janelas de vidros")
                print("5-Não confronte o intruso")
                print("6-Esteja preparado para a chegada da policia")
                print("7-Conheça as saidas de segurancas da sua universidade")
                print("8-Mantenha a calma\n")
                print("Menu pricipal\n")
                main()
            else:
                voltar_ao_menu = input("Voltar ao menu? (S/N)").upper()
                if voltar_ao_menu == "S":
                    main()
                else:
                    print("Programa encerrado.")
        else:
            print("Informações não confirmadas. Refazendo perguntas de emergência.")
            contagem_regressiva()
    elif ligar_para_policia == "N":
        print("Voltando ao menu.")
        main()
    else:
        print("Resposta inválida, programa encerrado")


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
            horario_saida = input("Digite o horário de saida do visitante (formato HH:MM): ")
            try:
                entrada = horario_entrada
                saida = horario_saida
                if entrada <= saida:
                    break
                else:
                    print("A hora de saida deve ser maior ou igual à hora de entrada. Tente novamente.")
            except ValueError:
                print("Formato de hora inválido. Use HH:MM. Tente novamente.")
                continue

        visitante = {
            'Nome': nome,
            'Idade': idade,
            'Documento': documento,
            'Motivo': motivo,
            'Entrada': entrada,
            'Saida': saida
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


""" função para salvar o visitante sem prescisar encerrar o programa """
def salvar_visitantes():
    salvar_dados(visitantes)
    print("Visitantes salvos com sucesso.")


""" função para pesquisar visitantes com o mesmo nome """
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
            print(f"Horário de saida: {visitante['Saida']}")
            print("-" * 20)
    else:
        print("Visitante não encontrado.")


""" função para editar os dados do visitante """
def editar_visitantes():
    caminho_arquivo_json = 'dados.json'

    alunos = carregar_dados()

    if not alunos:
        print("A lista de alunos está vazia. Não há alunos para editar.")
        return

    #lista os nomes dos alunos para saber qual nome editar
    print("Lista de Alunos:")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. {aluno['Nome']}")

    try:
        escolha = int(input("Digite o número do aluno que deseja editar: ")) - 1  #subtrai 1 para corresponder ao índice da lista

        #verifica se a escolha do usuário está dentro dos limites
        if 0 <= escolha < len(alunos):
            aluno = alunos[escolha]

            #fazer as ediçoes
            aluno['Nome'] = input(f"Nome atual: {aluno['Nome']}. Novo nome: ")
            aluno['Idade'] = int(input(f"Idade atual: {aluno['Idade']}. Nova idade: "))
            aluno['Documento'] = input(f"CPF atual: {aluno['Documento']}. Novo CPF: ")
            aluno['Entrada'] = input(f"Hora de entrada atual: {aluno['Entrada']}. Nova hora de entrada (formato HH:MM): ")
            aluno['Saida'] = input(f"Hora de saída atual: {aluno['Saida']}. Nova hora de saída (formato HH:MM): ")
            aluno['Motivo'] = input(f"Motivo atual: {aluno['Motivo']}. Novo motivo: ")

            #salvar as alterações no arquivo JSON
            salvar_dados(alunos)
            print("Edições salvas com sucesso.")

            #atualize o objeto visitantes após as edições
            visitantes.clear()
            visitantes.extend(alunos)
            
        else:
            print("Escolha inválida. O número do aluno não existe na lista.")
    except ValueError:
        print("Escolha inválida. Digite um número válido.")

    input("Pressione Enter para continuar após editar os alunos.")
    

""" função principal do menu """
def main():
    while True:
        exibir_menu()
        opcao = input("O que deseja escolher: ")
        if opcao == "1":
            registrar_visitante()
        elif opcao == "2":
            pesquisar_visitante()
        elif opcao == "3":
            editar_visitantes()
        elif opcao == "4":
            salvar_visitantes()
        elif opcao == "0":
            salvar_dados(visitantes)
            print("Programa encerrado")
            break
        else:
            print("Opção inválida. Tente novamente.")

""" iniciar o programa """
if __name__ == "__main__":
    try:
        tem_emergencia = input("Tem alguma emergência? (S/N)").upper()
        if tem_emergencia == "S":
            contagem_regressiva()
        elif tem_emergencia == "N":
            main()
        else:
            print("Resposta inválida, programa encerrado")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
