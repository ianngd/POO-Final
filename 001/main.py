import func as f
carros = [] 
opc = 0
op2 = 0

while True:
    try:
        opc = f.menu()

        if 0 == opc: 
            break
        
        if 1 == opc:
            _marca = input ('Marca: ')
            _modelo = input ('Modelo: ')
            _ano = input ('Ano: ')
            _cor = input ('Informe a cor: ')
            opc = int(input('--FINALIDADE--\n1 - Carro para entregas\n2 - Carro para transporte de pessoas: '))
            if 1 == opc:
                _finalidade = 'ENTREGAS'
            if 2 == opc:
                _finalidade = 'TRANSPORTE'
            carro = f.Carro(_finalidade, _marca, _modelo, _ano, _cor)
            carros.append(carro)
            print('\nCarro inserido com sucesso.\n')

        elif 2 == opc: #Selecionar carro
            op = int (input('Posição do carro: '))
            carro_selec =  carros[op-1]
            while op2 != 4:
                op2 = f.menu_2()
                if 1 == op2: # ligar motor
                    carro_selec.ligar_motor()
                if 2 == op2: # acelerar
                    carro_selec.acelerar()
                if 3 == op2: #painel
                    carro_selec.status_motor_painel()

        elif 3 == opc: #visualizar
            op = int (input('Qual a posição do carro:'))
            carro = carros[op - 1]
            f.print_carro(carro)
        
        elif 4 == opc: #Buscar
            subopc = int (input('Deseja buscar por:\n1 - Marca\n2 - Modelo\n3 - Ano\n4 - Cor\n5 - Finalidade: '))
            if 1 == subopc:
                marca = input('Informe a marca: ')
                marca = marca.upper()
                for car in carros:
                    if marca == car.marca:
                        f.print_carro(car)
                    
            elif 2 == subopc:
                modelo = input('Modelo: ')
                modelo = modelo.upper()
                for car in carros:
                    if modelo == car.modelo:
                        f.print_carro(car)
            elif 3 == subopc:
                ano = int(input('Informe ano com 4 digitos: '))
                for car in carros:
                    if ano == car.ano:
                        f.print_carro(car)
            elif 4 == subopc:
                cor = input('Informe a cor: ')
                cor = cor.upper()
                for car in carros:
                    if cor == car.cor:
                        f.print_carro(car)

            elif 5 == subopc:
                finalidade = int(input('--FINALIDADE--\n1 - Carro para entregas\n2 - Carro para transporte de pessoas: '))
                if 1 == finalidade:
                    for car in carros:
                        if 'ENTREGAS' == car.finalidade:
                            f.print_carro(car)
                if 2 == finalidade:
                    for car in carros:
                        if 'TRANSPORTE' == car.finalidade:
                            f.print_carro(car)
    except:
        print ('\n------\nOps! Erro no sistema. Por favor, tente novamente\n------\n')