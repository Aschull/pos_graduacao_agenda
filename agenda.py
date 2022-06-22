import os


def clear(): return os.system('cls')


contatos = []


class Agenda(object):
    def __init__(self, id, nome, telefone, cidade, estado, status):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        self.status = status

    def __repr__(self):
        return 'Contato: <ID: {}, Nome: {}, Telefone: {}, Cidade: {}, Estado: {}, Status: {}>'.format(
            self.id, self.nome, self.telefone, self.cidade, self.estado, self.status)


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
    while True:
        if status.upper() == 'P' or status.upper() == 'C':
            break
        else:
            print('ERRO: Valor invalido!')
            print('Valores validos: P -> Pessoal, C -> Comercial')
            status = input("Pessoal ou Comercial: ")
    agenda = Agenda(id, nome, telefone, cidade, estado, status)
    return agenda


def insere_contato():
    clear()
    contato = cria_contato()
    contatos.append(contato)
    print(f'<{contato.nome}> inserido com sucesso!')
    input('Enter para voltar ao menu!')


def altera_contato():
    clear()
    nome = input('Informe o nome do contato: ')
    for contato in contatos:
        if contato.nome == nome:
            id = contato.id
            nome = input("Escreva seu nome: ")
            telefone = input("Escreva seu telefone: ")
            cidade = input("Escreva sua cidade: ")
            estado = input("Escreva seu estado: ")
            status = input("Pessoal ou Comercial: ")
            while True:
                if status.upper() == 'P' or status.upper() == 'C':
                    break
                else:
                    print('ERRO: Valor invalido!')
                    print('Valores validos: P -> Pessoal, C -> Comercial')
                    status = input("Pessoal ou Comercial: ")
            agenda = Agenda(id, nome, telefone, cidade, estado, status)
            contatos[contatos.index(contato)] = agenda
            break
        else:
            print(f'Pessoa com o nome {nome} não encontrada')
    input('Enter para voltar ao menu!')


def lista_contatos():
    clear()
    if len(contatos) == 0:
        print('Agenda vazia!')
    else:
        for contato in contatos:
            print(contato)
    input('Enter para voltar ao menu!')


def procura_contato():
    clear()
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
    clear()
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
            print('Cadastro excluído')
        input('Enter para voltar ao menu!')
    else:
        print(f'Pessoa com o nome {nome} não encontrada')
        input('Enter para voltar ao menu!')
        return


def sair():
    clear()
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
    else:
        print('Erro: opção inválida!')
        input('Enter para voltar ao menu!')
