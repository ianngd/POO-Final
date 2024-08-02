class Ong ():
    nome = ''
    projetos = []

    def __init__(self,nome, projetos = 'None'):
        self.nome = nome.upper()
        self.projetos = projetos

    def adicionar_projeto(self, projeto): #adiciona um objeto Projeto à lista de projetos da ONG.
        self.projeto.append(projeto)
        
    def listar_projetos(self): #retorna uma lista com os nomes de todos os projetos da ONG.
        if self.projetos:
            for projeto in self.projetos:
                print (f'PROJETO: {self.nome}\n')
        else:
            print ('Não há projetos inscritos nesta ONG')      

    def buscar_projeto(self, nome): #retorna o objeto Projeto com o nome especificado, se existir, ou None caso contrário
        nome = nome.upper()
        for projeto in self.projetos:
            if projeto.nome.upper() == nome:
                return projeto
            else:
                return None
            
class Projeto ():
    nome = ''
    descricao = ''
    responsavel = ''
    status = ''
    
    def __init__(self, nome, descricao, responsavel, status): # inicializa os atributos do projeto.
        self.nome = nome.upper()
        self.descricao = descricao.upper()
        self.responsavel = responsavel.upper()
        self.status = status.upper()

    def mostrar_informacoes (self): # retorna uma string com todas as informações do projeto.
        print (f'PROJETO: {self.nome}\nDESCRCICAO: {self.descricao}\nRESPONSAVEL: {self.responsavel}\nSTATUS: {self.status}')

    def atualizar_status(self, novo_status): #atualiza o status do projeto.
        self.status = novo_status
        print('\nStatus atualizado com sucesso.\n')
        self.mostrar_informacoes ()
def menu(opc = 'None'):
    print ('========================================')
    print ('0 - SAIR')
    print ('1 - ONG - CADASTRAR')
    print ('2 - ONG - LISTAR PROJETOS')
    print ('3 - ONG - BUSCAR PROJETO POR NOME')
    print ('4 - PROJETO - CADASTRAR')
    print ('5 - PROJETO - ATUALIZAR STATUS')
    print ('6 - PROJETO - MOSTRAR DETALHES')
    print ('========================================')
    opc = int(input ('>>> '))
    

    return opc
# No arquivo aa1.py

def cadastrar_projeto():
    nome = input('NOME DO PROJETO: ')
    descricao = input('DESCREVA O PROJETO: ')
    responsavel = input('NOME DO RESPONSÁVEL: ')
    
    try:
        pre_status = int(input('STATUS DO PROJETO: \n1 - PENDENTE\n2 - EM ANDAMENTO\n3 - CONCLUÍDO\nEscolha uma opção: '))
        if pre_status == 1:
            status = 'PENDENTE'
        elif pre_status == 2:
            status = 'EM ANDAMENTO'
        elif pre_status == 3:
            status = 'CONCLUÍDO'
        else:
            print('Opção inválida. Definindo como PENDENTE por padrão.')
            status = 'PENDENTE'
    except ValueError:
        print('Valor inválido. Definindo como PENDENTE por padrão.')
        status = 'PENDENTE'
    
    return Projeto(nome, descricao, responsavel, status)

def buscar_ong(ongs):
    nome = input('NOME DA ONG: ').upper()
    for ong in ongs:
        if ong.nome == nome:
            print(f'Nome da ONG: {ong.nome}')
            print('Projetos:')
            Ong.listar_projetos()
            return ong.nome
    print('ONG não encontrada.')


