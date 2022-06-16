from app.entities.agenda import Agenda
import os


def clear(): return os.system('cls')


contatos = []


def create_menu():
    print(
        ' \
        1. Cadastrar Pessoa na Agenda \n \
        2. Alterar dados da Pessoa \n \
        3. Listar Agenda \n \
        4. Procurar pessoa na Agenda \n \
        5. Excluir Pessoa da Agenda \n \
        6. Sair do sistema'
    )


def cria_contato():
    id = (len(contatos)+1)
    nome = input("Escreva seu nome: ")
    telefone = input("Escreva seu telefone: ")
    cidade = input("Escreva sua cidade: ")
    estado = input("Escreva seu estado: ")
    status = input("Pessoal ou Comercial: ")
    agenda = Agenda(id, nome, telefone, cidade, estado, status)
    return agenda


def insere_contato():
    contato = cria_contato()
    contatos.append(contato)
    print(f'<{contato.nome}> inserido com sucesso!')
    input('Enter para voltar ao menu!')


def altera_contato():
    nome = input('Informe o nome do contato: ')
    for contato in contatos:
        if contato.nome == nome:
            id = contato.id
            nome = input("Escreva seu nome: ")
            telefone = input("Escreva seu telefone: ")
            cidade = input("Escreva sua cidade: ")
            estado = input("Escreva seu estado: ")
            status = input("Pessoal ou Comercial: ")
            agenda = Agenda(id, nome, telefone, cidade, estado, status)
            contatos[contatos.index(contato)] = agenda
            break
        else:
            print(f'Pessoa com o nome {nome} não encontrada')
    input('Enter para voltar ao menu!')


def lista_contatos():
    if len(contatos) == 0:
        print('Agenda vazia!')
    else:
        for contato in contatos:
            print(contato)
    input('Enter para voltar ao menu!')


def procura_contato():
    nome = input('Informe o nome do contato: ')
    nomes = []
    existe = False
    for contato in contatos:
        if contato.nome == nome:
            nomes.append(contato)
            existe = True

    if existe:
        for nome in nomes:
            print(nome)
        input('Enter para voltar ao menu!')
    else:
        print(f'Pessoa com o nome {nome} não encontrada')
        input('Enter para voltar ao menu!')
        return


def exclui_contato():
    nome = input('Informe o nome do contato: ')
    nomes = []
    existe = False
    for contato in contatos:
        if contato.nome == nome:
            nomes.append(contato)
            existe = True

    if existe:
        for nome in nomes:
            contatos.remove(nome)
        input('Enter para voltar ao menu!')
    else:
        print(f'Pessoa com o nome {nome} não encontrada')
        input('Enter para voltar ao menu!')
        return


def sair():
    exit()


while True:
    clear()
    create_menu()
    opcao = int(input("Opcao: "))
    if opcao == 1:
        insere_contato()
    elif opcao == 2:
        altera_contato()
    elif opcao == 3:
        lista_contatos()
    elif opcao == 4:
        procura_contato()
    elif opcao == 5:
        exclui_contato()
    elif opcao == 6:
        sair()
