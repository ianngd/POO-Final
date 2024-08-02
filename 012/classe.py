import random

class Animal ():
    coracao:bool
    racional:bool

    def __init__(self,nome, coracao, cor,racional,sexo, tempo_gestacao):
        self.nome = nome.upper()
        self.coracao = coracao
        self.cor = cor.upper()
        self.racional = racional
        self.sexo = sexo.upper()
        self.tempo_gestacao = tempo_gestacao.upper()


class Humano (Animal):
    def __init__(self,nome,cor,sexo,nacionalidade,sobrenome,grau_instrucao):
        super().__init__(nome, True, cor, True, sexo, '9 meses')
        self.nacionalidade = nacionalidade.upper()
        self.sobrenome = sobrenome.upper()
        self.grau_instrucao = grau_instrucao.upper()


    def visualizar_humano(self):
        print(f'\nNOME: {self.nome} {self.sobrenome}')
        print(f'COR: {self.cor}')
        print(f'SEXO: {self.sexo}')
        print(f'NACIONALIDADE: {self.nacionalidade}')
        print(f'INSTRUÇÃO: {self.grau_instrucao}')
        print('CORAÇÃO: SIM')
        print ('RACIONAL: SIM')
        if self.sexo == 'MASCULINO':
            pass
        else:
            print(f'TEMPO DE GESTAÇÃO: {self.tempo_gestacao}')

class Cachorro (Animal):
    idade = 0

    def __init__(self, nome,cor,sexo, porte, idade, raça):
        super().__init__(nome, True, cor, False, sexo,'68 dias')
        self.porte = porte.upper()
        self.idade = idade
        self.raça = raça.upper()
        
    def latir (self):
        print ("Au au")

    def acordado_dormindo(self):
        acordado = bool(random.getrandbits(1))
        if acordado:
            self.latir()
        else:
            print(f'{self.nome} está dormindo. Tente novamente mais tarde.\n')

    def visualizar_dog(self):
        print(f'\nNOME: {self.nome}')
        print('CORAÇÃO: SIM')
        print(f'COR: {self.cor}')
        print ('RACIONAL: NÃO')
        print(f'SEXO: {self.sexo}')
        print(f'TEMPO DE GESTAÇÃO: {self.tempo_gestacao}')
        print(f'PORTE: {self.porte}')
        print(f'IDADE: {self.idade}')
        print(f'RAÇA: {self.raça}\n')

#dog = Cachorro('Dora', 'marrom', 'fêmea', 'médio', '3 ANOS', 'não definida')
#humano = Humano('Iann','Parda','feminino','brasileiro','Domingos','Ensino Superior')
#dog.latir()
#humano.visualizar_humano()
#dog.visualizar_dog()
#dog.acordado_dormindo()