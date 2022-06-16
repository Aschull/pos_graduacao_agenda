class Agenda(object):
    def __init__(self, id, nome, telefone, cidade, estado, status):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        self.status = status

    def __repr__(self):
        return 'Contato: <ID: {}, Nome: {}, Telefone: {}, Cidade: {}, Estado: {}, Status: {}>'.format(self.id, self.nome, self.telefone, self.cidade, self.estado, self.status)
