class Ong:
    def __init__(self, nome, projetos=None):
        self.nome = nome.upper()
        self.projetos = [] if projetos is None else projetos

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def listar_projetos(self):
        if self.projetos:
            for projeto in self.projetos:
                print(f'PROJETO: {projeto.nome}\n')
        else:
            print('Não há projetos inscritos nesta ONG')

    def buscar_projeto(self, nome):
        nome = nome.upper()
        for projeto in self.projetos:
            if projeto.nome == nome:
                return projeto
        return None

class Projeto:
    def __init__(self, nome, descricao, responsavel, status):
        self.nome = nome.upper()
        self.descricao = descricao.upper()
        self.responsavel = responsavel.upper()
        self.status = status.upper()

    def mostrar_informacoes(self):
        return f'PROJETO: {self.nome}\nDESCRIÇÃO: {self.descricao}\nRESPONSÁVEL: {self.responsavel}\nSTATUS: {self.status}'

    def atualizar_status(self, novo_status):
        self.status = novo_status
        print('\nStatus atualizado com sucesso.\n')

# Código de teste
ong = Ong('Rios limpos')

projeto1 = Projeto('Salve os rios', 'Tentando salvar rios', 'Iann Gabriel', 'Em andamento')
ong.adicionar_projeto(projeto1)

projeto2 = Projeto('Salve árvores', 'Tentando salvar árvores', 'Iann Gabriel', 'Concluído')
ong.adicionar_projeto(projeto2)

ong.listar_projetos()

projeto_valido = ong.buscar_projeto('Salve os rios')
if projeto_valido is not None:
    print(f'Projeto: {projeto_valido.nome}')
    print(f'Status: {projeto_valido.status}')

projeto_valido.atualizar_status('Concluído')
print(f'Status Atualizado: {projeto_valido.status}')

info_projeto = projeto_valido.mostrar_informacoes()
print(f'Informações do Projeto:\n{info_projeto}')
