import aa1 as f
ongs = []
opc = 1


while opc != 0  :
    try:

        opc = f.menu()

        if 1 == opc: # Cadastrar ONG
            nome_ong = input ('NOME DA ONG: ')
            try:
                adiciona = int(input ('ADICIONAR PROJETO?\n1 - SIM\n2 - NAO: '))
                if adiciona == 1:
                    temp = []
                    temp = f.cadastrar_projeto()
                    ong = f.Ong (nome_ong, temp)
                    ongs.append(ong)
                elif adiciona == 2:
                    ong = f.Ong(nome_ong)
                    ongs.append(ong)
                    print ('\nOK! VOCE PODE CADASTRAR A ONG POSTERIORMNETE')
                else:
                    print ('\nOPCAO INVALIDA. POR FAVOR, TENTE NOVAMENTE\n')
            except:
                pass      
        elif 2 == opc: #Listar projetos da ONG
            pass
        elif 3 == opc: #Buscar projeto da ong por nome
            pass
        elif 4 == opc: #Cadastrar projeto
            nome = f.buscar_ong([ongs])
            if nome != None:
                for nome in ongs:
                    if ongs.nome == nome:
                        temp = f.cadastrar_projeto()
                        ongs.projetos.append(temp)
                        print ('Projeto adicionado com sucesso')
            elif subopc == 2:
                    nome_ong = input ('NOME DA ONG: ')
                    temp = []
                    temp = f.cadastrar_projeto()
                    ong = f.Ong (nome_ong, temp)
                    ongs.append(ong)
                
        elif 5 == opc: #Atualizar status de projeto
            pass
        elif 6 == opc: #Mostrar detalhes de um projeto especifico
            pass
        else:
            print ('Opcao Invalida. Por favor, tente novamente\n')

    except:
        print ('Erro sistemico. Por favor, tente novamente.')
        
#         nome_da_ong = "Minha ONG"
#         lista_de_projetos = ["Projeto 1", "Projeto 2", "Projeto 3"]

#         minha_ong = f.Ong(nome_da_ong, lista_de_projetos)

#         print(minha_ong.nome)
#         print(minha_ong.projetos[0])







# # Exemplo de uso:
# projeto1 = Projeto('Projeto A', 'Descrição do Projeto A', 'Fulano', 'Em andamento')
# projeto1.mostrar_informacoes()

# # Atualizando o status do projeto
# projeto1.atualizar_status('Concluído')

#     # Criando uma ONG e adicionando projetos
#     ong = Ong("Minha ONG", [])
#     projeto1 = Projeto("Projeto A", "Descrição do Projeto A", "João", "Em andamento")
#     projeto2 = Projeto("Projeto B", "Descrição do Projeto B", "Maria", "Concluído")

#     ong.adicionar_projeto(projeto1)
#     ong.adicionar_projeto(projeto2)

#     # Listando os projetos da ONG
#     ong.listar_projetos()

#     # Buscando um projeto pelo nome
#     nome_procurado = "Projeto A"
#     projeto_encontrado = ong.buscar_projeto(nome_procurado)
#     if projeto_encontrado:
#         print(f'Projeto encontrado: {projeto_encontrado.nome}')
#     else:
#         print(f'Projeto com nome "{nome_procurado}" não encontrado.')


