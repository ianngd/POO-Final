from classe import *
from views  import *
import os

cachorros = []
humanos = []

def criar_cachorro ():
    
    nome = input ('Digite o nome do cachorro: ')
    cor = input ('Qual a cor do cachorro: ')
    menu_sexo_dog()
    sexo = int(input('>>> '))
    if sexo == 1:
        sexo_cao = 'Femea'
    elif sexo == 2:
        sexo_cao = 'Macho'
    else: 
        print ('Opção invalida. Atribuidoo automaticamente como macho.')
        sexo_cao = 'Macho'
    menu_porte_dog()
    porte = int(input('>>> '))
    if porte == 1:
        porte_cao = 'Grande'
    elif porte == 2:
        porte_cao = 'Médio'
    elif porte == 3:
        porte_cao = 'Pequeno'
    else: 
        print ('Opção invalida. Atribuidoo automaticamente como macho.')
        porte_cao = 'Médio'
    idade_cao = input('Quantos anos (Ex: 1): ')
    meses_cao = input('E quantos meses (Ex: 7 ): ')
    idade = idade_cao +' anos e ' + meses_cao +' meses.'
    raça = input ('Informe a raça do cachorro: ')
    dog = Cachorro(nome,cor,sexo_cao,porte_cao,idade,raça)
    cachorros.append(dog)   
    print('\nSeu cachorro foi criado com sucesso.\n')
def criar_humano ():
    nome = input ('Qual o nome da pessoa: ')
    sobrenome = input ('Informe também o sobrenome: ')
    menu_cor()
    opc_cor = int(input('>>> '))
    if opc_cor == 1:
        cor = 'branca'
    elif opc_cor == 2:
        cor = 'Parda'
    elif opc_cor == 3:
        cor = 'Preta'
    elif opc_cor == 4:
        cor = 'Amarela'
    else:
        print('Seleção invalida. Atribuido automaticamente a cor Parda.')
        cor = input('parda')
    menu_sexo_humano()
    opc_sexo = int(input('>>> '))
    if opc_sexo == 1:
        sexo = 'Masculino'
    elif opc_sexo == 2:
        sexo = 'Feminino'
    elif opc_sexo == 3:
        sexo = 'Prefiro não responder'
    else:
        print('Opção invalida. Atribuido automaticamente Prefiro não responder.')
        sexo = input('Prefiro não responder')
    nacionalidade = input ('\nQual a nacionalidade: ')
    menu_instrucao()
    i = int (input('>>> '))
    if i == 1:
        graduacao = 'Ensino fundamental'
    elif i == 2:
        graduacao = 'Ensino Médio'
    elif i == 3:
        graduacao = 'Ensino Técnico'
    elif i == 4: 
        graduacao = 'Ensino Superior'
    else:
        print('\nOpção digitada invalida. Atribuido automaticamente Ensino Fundamental.')
        graduacao = 'Ensino fundamental'
    
    humano = Humano(nome,cor,sexo,nacionalidade,sobrenome,graduacao)
    humanos.append(humano)
    print('\nHumano criado com sucesso!')


while True:
    print ("===== TESTE ===== ")
    menu_principal()
    opc = int (input('>>> '))
    os.system('cls')
    if opc == 0:
        break
    elif opc == 1:
        menu_humano_principal()
        opc = int(input('>>> '))
        os.system('cls')

        if opc == 0 or opc > 2:
            pass
        elif opc == 1:
            criar_humano()
        elif opc == 2:
            for humano in humanos:
                humano.visualizar_humano()
        else:
            pass

    elif opc == 2:
        menu_dog_principal()
        opc = int(input('>>> '))
        os.system('cls')
        if opc == 0 or opc > 3:
            pass
        elif opc == 1: 
            criar_cachorro()

        elif opc == 2:
            for cachorro in cachorros:
                cachorro.visualizar_dog()

        elif opc == 3:
            for cachorro in cachorros:
                cachorro.acordado_dormindo()
        else:
            pass
        

