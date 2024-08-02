class Base ():
    marca = ''
    modelo = ''
    ano = 0 
    cor = ''
    status_motor = False
    velocidade = 0

    def __init__(self,_marca,_modelo,_ano,_cor): #init em outras linguagens é chamada de construtor / constructor
        self.marca = _marca.upper()
        self.modelo = _modelo.upper()
        self.ano = _ano
        self.cor = _cor.upper()

class Carro(Base): #aqui criando uma classe frota que herda os atributos e as classes do Carro
    _finalidade = ''
    def __init__(self, _finalidade, _marca, _modelo, _ano, _cor):
        self.finalidade = _finalidade.upper()
        super().__init__(_marca, _modelo, _ano, _cor)

    def ligar_motor (self):
        print ('Motor ligado!')
        self.status_motor = True

    def desligar_motor (self):
        print ('Motor desligado!')
        self.status_motor = False
    def acelerar (self):
        print ('Carro Acelerando')

    def status_motor_painel(self):
        if self.status_motor == True:
            print('Este carro está ligado.\n')
        else:
            print('Este carro está desligado.\n')

    def acelerar (self):
        if self.status_motor == True:
            for vel in range (0,10):
                self.velocidade +=10
                print ('Velocidade',self.velocidade)
            print ('Carro acelerando')
        else: 
            print ('Seu carro não está ligado. ')

def menu ():
    opc = int(input ('\n0 - Sair\n1 - Criar Carro\n2 - Selecionar Carro\n3 - Visualizar\n4 - Buscar: '))
    return opc

def menu_2():
    opc = int(input ('\n1 - Ligar o Motor\n2 - Acelerar\n3 - Painel\n4 - Sair: '))
    return opc 

def print_carro(carro):
    print (f'\n Carro da marca {carro.marca}, do modelo {carro.modelo}.\nAno de fabricaçao foi {carro.ano} na cor  {carro.cor}.\n')
    print (f'Carro utilizado para {carro.finalidade}.')