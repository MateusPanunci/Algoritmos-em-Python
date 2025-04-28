import os, time, random, copy


def limpatela():
    os.system('cls')


def tempo(z):
    time.sleep(z)
    limpatela()

def tutorial():
    limpatela()
    print("---------------------------------------\n             Batalha naval\n---------------------------------------\n")
    print("        Escolha o tutorial visado\n\n(1) Modo 1 jogador      (2) Modo 2 jogadores\n")
    while True:
        modo = str(input("Opção "))
        if modo != "1" and modo != "2": 
            print("\nDigite uma opção existente!")
            continue
        else: break

    limpatela()
    
    print("---------------------------------------\n             Batalha naval\n---------------------------------------\n")
    if modo == "1": 
        print("Objetivo: afundar todos os navios do tabuleiro dentro do número de tentativas disponíveis.\n")
        print("Como atirar: insira as coordenadas que você deseja atacar. Ex: A1, B4, I10\n")
        print("Símbolos\n  °: Não há barco nesta coordenada\n  ~: Mar (não há barco)\n  X: Parte destruída\n\n  ")
    
    else:
        print("Objetivo: cada jogador alterna turnos de tiros para exterminar a marinha do outro e se consagrar o rei dos mares !!!\n")
        print("Como atirar: insira as coordenadas que você deseja atacar. Ex: A1, B4, I10\n")
        print("Símbolos\n  °: Não há barco nesta coordenada\n  ~: Mar (não há barco)\n  X: Parte destruída\n\n  ")

    input("Clique ENTER para voltar ao menu inicial")

def modo_de_jogo():
    limpatela()
    print("---------------------------------------\n             Batalha naval\n---------------------------------------\n")
    print("        Escolha um modo de jogo\n\n(1) Um jogador      (2) Dois jogadores\n")
    while True:
        modo = str(input("Opção "))
        if modo != "1" and modo != "2": 
            print("\nDigite uma opção existente!")
            continue


        return modo

def menu_incial():
    print("           Domine os Mares!!!\n\n      (1) Jogar      (2) Tutorial\n")
    while True:
        escolha = str(input("Opção "))
        if escolha != "1" and escolha != "2": 
            print("\nDigite uma opção existente!")
            continue
        else: break

    return escolha
    

def modo_um_player():
    def dificuldade():
        print(f"{"-" * 38}\n           Modo um jogador\n{"-" * 38}\n")
        print("  Escolha a dificuldade:\n\n(1) Fácil: 50 tentativas\n(2) Médio: 42 tentativas\n(3) Difícil: 35 tentativas\n")
        while True:
            modo = input("Opção ")
            if modo == "1": 
                tentativas = 50
            elif modo == "2":
                tentativas = 42
            elif modo == "3":
                tentativas = 35
            else:
                print("\nDigite uma opção existente!")
                continue
            break
        return tentativas

    def cria_tabuleiro():   
        tab = [[" " for _ in range(10)] for _ in range(10)]
        return tab


    def posiciona_navios():
        def sobrepostas(parte, navios):
            for barco in navios:
                if parte in barco:
                    return True
            return False
        
        def verifica_em_volta(parte, navios):
            ocupado, cont = [], 3
            parte_list = [caract for caract in parte]

            while cont > 0:
                if cont == 3:
                    select = -1
                elif cont == 2:
                    select = 0
                else:
                    select = 1
                
                
                lista = parte_list.copy()
                lista = [int(num) for num in lista]
                lista[0] += select

                
                for z in range(0,3):
                    verifica = lista[1] + z - 1
                    coordenada = f"{lista[0]}{verifica}"
                    

                    if coordenada == parte: 
                        continue
                    else:
                        for barco in navios:
                            if coordenada not in barco:
                                continue
                            else:
                                ocupado.append(True)
                        
                cont -= 1

            return ocupado
        

        navios, navio, cont, celulas = [], [], 7, 5
        while cont != 0:
            navio = []


            while True:
                orientacao = random.randint(1,2)
                repetido, redondezas = [], []


                if orientacao == 1:
                        linha = random.randint(0, 9)
                        coluna = random.randint(0, 5)         
                        for k in range(0, celulas):
                            parte = f"{linha}{coluna + k}"
                            repetido.append(sobrepostas(parte, navios))
                            redondezas.append(verifica_em_volta(parte, navios))
                            navio.append(parte)


                if orientacao == 2:
                        linha = random.randint(0, 5)
                        coluna = random.randint(0, 9)   
                        for k in range(0, celulas):
                            parte = f"{linha + k}{coluna}"
                            repetido.append(sobrepostas(parte, navios))
                            redondezas.append(verifica_em_volta(parte, navios))
                            navio.append(parte)
                    

                verdade = 0
                for part in redondezas:
                    if True in part:
                        verdade += 1


                if verdade == 0 and True not in repetido:
                    navios.append(navio)
                    break
                else:
                    navio.clear()

            
            if cont < 5 and cont % 2 == 1:
                celulas -= 1
            elif cont >= 5:
                celulas -= 1
            
            cont -= 1

        return navios


    def jogo(tentativas, navios, tab):
        def mostra_tabuleiro(tab):
            letras = "     A    B    C    D    E    F    G    H    I    J\n"
            print(letras)
            
            for i, line in enumerate(tab):
                if i == 9:
                    print(f"{i + 1}   {"    ".join(line)}\n")
                else:
                    print(f" {i + 1}   {"    ".join(line)}\n")
        

        def processa_jogada(tiro, navios):
                acerto = False
                try:
                    tiro_lista = [caract for caract in tiro]

                    tiro_lista[0] = ord(tiro_lista[0].upper()) - (ord("A"))

                    # Se a letra for diferente das do tabuleiro
                    if tiro_lista[0] > 9:
                        raise
                    else:
                        tiro_lista[0] = str(tiro_lista[0])
                    
                    #Se tem um 10 
                    if len(tiro_lista) == 3:
                        tiro_lista[1] = str(int("".join([tiro_lista[1], tiro_lista[2]])) - 1)
                        
                    elif len(tiro_lista) == 2:   
                        tiro_lista[1] = str(int(tiro_lista[1]) - 1)
                    else:
                        raise

                    
                
                
                    tiro_certo = tiro_lista[1], tiro_lista[0]
                    verificador = "".join(tiro_certo)


                except BaseException:
                    print(" !!!!! Você inseriu a coordenada de maneira incorreta, tente novamente !!!!!\n ")
                    return ""
                    

                for navio in navios:
                    for parte in navio:
                        if parte == verificador:
                            navio.remove(parte)
                            if navio == []:
                                navios.remove(navio)
                                destruido = True
                            else:
                                destruido = False
                            acerto = True 
                            break


                if acerto == False: 
                    return ["*", verificador]
                else:
                    if destruido == True:
                        return ["!", verificador]
                    else:
                        return verificador


        def atualiza_tab(jogada, tab, frota):
            def sem_barcos_em_volta(i, j, diagonais = True): 
                if diagonais == True: #Diagonais é para ver se coloca "°" apenas nelas ou não
                    cont = 4
                    while cont > 0:
                        if cont % 2 == 0:
                            select_j = -1
                        else: 
                            select_j = 1
                        

                        if cont > 2:
                            select_i = -1
                        else:
                            select_i = 1
                        

                        select_i += i
                        select_j += j
                        

                        if select_i >= 0 and select_j >= 0 and select_i < 10 and select_j < 10:   
                            tab[select_i][select_j] = "°"       

                        cont -= 1
                
                
                else:
                    cont = 3

                    while cont > 0:
                        if cont == 3:
                            select_i = -1
                        elif cont == 2:
                            select_i = 0
                        else:
                            select_i = 1
                        
                        
                        select_i += i
                        for z in range(0,3):
                            select_j = j + z - 1

                            if select_i >= 0 and select_j >= 0 and select_i < 10 and select_j < 10:
                                if select_i != i or select_j != j: 
                                    if tab[select_i][select_j] == "~" or tab[select_i][select_j] == " ":
                                        tab[select_i][select_j] = "°"

                        cont -= 1
                        

            def navio_destruido(parte):
                for barco in frota:
                    if parte in barco:
                        if len(barco) > 1:
                            index = [0, -1]
                            for ind in index:                
                                coordenada_lista = [int(caract) for caract in barco[ind]]
                                i, j = coordenada_lista
                                sem_barcos_em_volta(i, j, False)
                        else:
                            coordenada_lista = [int(caract) for caract in barco[0]]
                            i, j = coordenada_lista
                            sem_barcos_em_volta(i, j, False)
            
            
            if jogada == "":
                return None
            

            elif "*" in jogada:
                jogada_lista = [int(caract) for caract in jogada[1]]
                i, j = jogada_lista
                if tab[i][j] == "°":
                    print("!!!! Já foi lhe informado que não há navios nesta coordenada !!!!")
                elif tab[i][j] != " ":
                    print("!!!! Você já executou um tiro nesta coordenada !!!!")
                    return "já atirou"
                else:
                    print(" - ~~~~~ -  Você acertou a água ! - ~~~~~ - ")
                    tab[i][j] = "~"
                

            elif "!" in jogada:
                jogada_lista = [int(caract) for caract in jogada[1]]
                i, j = jogada_lista
                tab[i][j] = "X"
                print(" - XXXXX - Você destruiu um navio ! - XXXXX -")
                navio_destruido(jogada[1])


            else:
                coordenada_lista = [int(caract) for caract in jogada]
                i, j = coordenada_lista
                tab[i][j] = "X"
                print(" - +++++ - Você acertou um navio ! - +++++ -")
                sem_barcos_em_volta(i, j)
        
    
        frota = copy.deepcopy(navios)
        while tentativas != 0 and len(navios) != 0:
            mostra_tabuleiro(tab)
            print(f"Navios no mar: {len(navios)}            Tentativas: {tentativas}\n")
            tiro = input("Tiro: ")
            limpatela()
            jogada = processa_jogada(tiro, navios)
            
            if jogada == "":
                z = 3
                tempo(z)
                continue
            else:
                z = 2
            atualizado = atualiza_tab(jogada, tab, frota)
            if atualizado != "já atirou":
                 tentativas -= 1
            tempo(z)

            
        return tentativas
            
   
    tentativas = dificuldade()     
    tabuleiro = cria_tabuleiro()
    navios = posiciona_navios()
    limpatela()
    tentativas = jogo(tentativas, navios, tabuleiro)


    if tentativas == 0:
        print("       --------- Você Perdeu ----------\n")
        print("     Desbravar os mares não é seu forte !")
    else:
        print("        ========= Parábens, Você Venceu ! =========")
        print("\nPelo seu desempenho, você se tornou um mestre dos mares!")



def modo_dois_players():
    def cria_tabuleiro():   
        tab = [[" " for _ in range(10)] for _ in range(10)]
        return tab


    def posiciona_navios():
        def sobrepostas(parte, navios):
            for barco in navios:
                    if parte in barco:
                        return True
            return False
        
        def verifica_em_volta(parte, navios):
            ocupado, cont = [], 3
            parte_list = [caract for caract in parte]

            while cont > 0:
                if cont == 3:
                    select = -1
                elif cont == 2:
                    select = 0
                else:
                    select = 1
                
                
                lista = parte_list.copy()
                lista = [int(num) for num in lista]
                lista[0] += select

                
                for z in range(0,3):
                    verifica = lista[1] + z - 1
                    coordenada = f"{lista[0]}{verifica}"
                    

                    if coordenada == parte: 
                        continue
                    else:
                        for barco in navios:
                            if coordenada not in barco:
                                continue
                            else:
                                ocupado.append(True)
                        
                cont -= 1

            return ocupado
        
        qtd_mapa, mapas = 2, []
        while True:
            navios, navio, cont, celulas = [], [], 7, 5
            while cont != 0:
                navio = []


                while True:
                    orientacao = random.randint(1,2)
                    repetido, redondezas = [], []


                    if orientacao == 1:
                            linha = random.randint(0, 9)
                            coluna = random.randint(0, 5)         
                            for k in range(0, celulas):
                                parte = f"{linha}{coluna + k}"
                                repetido.append(sobrepostas(parte, navios))
                                redondezas.append(verifica_em_volta(parte, navios))
                                navio.append(parte)


                    if orientacao == 2:
                            linha = random.randint(0, 5)
                            coluna = random.randint(0, 9)   
                            for k in range(0, celulas):
                                parte = f"{linha + k}{coluna}"
                                repetido.append(sobrepostas(parte, navios))
                                redondezas.append(verifica_em_volta(parte, navios))
                                navio.append(parte)
                        

                    verdade = 0
                    for part in redondezas:
                        if True in part:
                            verdade += 1


                    if verdade == 0 and True not in repetido:
                        navios.append(navio)
                        break
                    else:
                        navio.clear()

                
                if cont < 5 and cont % 2 == 1:
                    celulas -= 1
                elif cont >= 5:
                    celulas -= 1
                

                cont -= 1

            mapas.append(navios)
            qtd_mapa -= 1
            if qtd_mapa == 0:
                break


        return mapas[0], mapas[1]


    def jogo():
        def mostra_tabuleiro(tab):
            letras = "     A    B    C    D    E    F    G    H    I    J\n"
            print(letras)
            
            for i, line in enumerate(tab):
                if i == 9:
                    print(f"{i + 1}   {"    ".join(line)}\n")
                else:
                    print(f" {i + 1}   {"    ".join(line)}\n")
        

        def processa_jogada(tiro, navios):
                acerto = False
                try:
                    tiro_lista = [caract for caract in tiro]

                    tiro_lista[0] = ord(tiro_lista[0].upper()) - (ord("A"))

                    # Se a letra for diferente das do tabuleiro
                    if tiro_lista[0] > 9:
                        raise
                    else:
                        tiro_lista[0] = str(tiro_lista[0])
                    
                    #Se tem um 10 
                    if len(tiro_lista) == 3:
                        tiro_lista[1] = str(int("".join([tiro_lista[1], tiro_lista[2]])) - 1)
                        
                    elif len(tiro_lista) == 2:   
                        tiro_lista[1] = str(int(tiro_lista[1]) - 1)
                    else:
                        raise

                    
                
                
                    tiro_certo = tiro_lista[1], tiro_lista[0]
                    verificador = "".join(tiro_certo)


                except BaseException:
                    print(" !!!!! Você inseriu a coordenada de maneira incorreta, tente novamente !!!!!\n ")
                    return ""
                    

                for navio in navios:
                    for parte in navio:
                        if parte == verificador:
                            navio.remove(parte)
                            if navio == []:
                                navios.remove(navio)
                                destruido = True
                            else:
                                destruido = False
                            acerto = True 
                            break


                if acerto == False: 
                    return ["*", verificador]
                else:
                    if destruido == True:
                        return ["!", verificador]
                    else:
                        return verificador


        def atualiza_tab(jogada, tab, frota):
            def sem_barcos_em_volta(i, j, diagonais = True): 
                if diagonais == True: #Diagonais é para ver se coloca "°" apenas nelas ou não
                    cont = 4
                    while cont > 0:
                        if cont % 2 == 0:
                            select_j = -1
                        else: 
                            select_j = 1
                        

                        if cont > 2:
                            select_i = -1
                        else:
                            select_i = 1
                        

                        select_i += i
                        select_j += j
                        

                        if select_i >= 0 and select_j >= 0 and select_i < 10 and select_j < 10:   
                            tab[select_i][select_j] = "°"       

                        cont -= 1
                
                
                else:
                    cont = 3

                    while cont > 0:
                        if cont == 3:
                            select_i = -1
                        elif cont == 2:
                            select_i = 0
                        else:
                            select_i = 1
                        
                        
                        select_i += i
                        for z in range(0,3):
                            select_j = j + z - 1

                            if select_i >= 0 and select_j >= 0 and select_i < 10 and select_j < 10:
                                if select_i != i or select_j != j: 
                                    if tab[select_i][select_j] == "~" or tab[select_i][select_j] == " ":
                                        tab[select_i][select_j] = "°"

                        cont -= 1
                        

            def navio_destruido(parte):
                for barco in frota:
                    if parte in barco:
                        if len(barco) > 1:
                            index = [0, -1]
                            for ind in index:                
                                coordenada_lista = [int(caract) for caract in barco[ind]]
                                i, j = coordenada_lista
                                sem_barcos_em_volta(i, j, False)
                        else:
                            coordenada_lista = [int(caract) for caract in barco[0]]
                            i, j = coordenada_lista
                            sem_barcos_em_volta(i, j, False)
            
            
            if jogada == "":
                return None
            

            elif "*" in jogada:
                jogada_lista = [int(caract) for caract in jogada[1]]
                i, j = jogada_lista
                if tab[i][j] == "°":
                    print("!!!! Já foi lhe informado que não há navios nesta coordenada !!!!")
                    tempo(3)
                    return "!"
                elif tab[i][j] != " ":
                    print("!!!! Você já executou um tiro nesta coordenada !!!!")
                    tempo(3)
                    return "!"
                else:
                    print(" - ~~~~~ -  Você acertou a água ! - ~~~~~ - ")
                    tab[i][j] = "~"
                

            elif "!" in jogada:
                jogada_lista = [int(caract) for caract in jogada[1]]
                i, j = jogada_lista
                tab[i][j] = "X"
                print(" - XXXXX - Você destruiu um navio ! - XXXXX -")
                navio_destruido(jogada[1])


            else:
                coordenada_lista = [int(caract) for caract in jogada]
                i, j = coordenada_lista
                tab[i][j] = "X"
                print(" - +++++ - Você acertou um navio ! - +++++ -")
                sem_barcos_em_volta(i, j)
        
        def jogador_1(navios, tab, frota):
                while True:
                    limpatela()
                    print("           ----------- Jogador 1 -----------\n")
                    mostra_tabuleiro(tab)
                    print(f"Navios no mar: {len(navios)}")
                    tiro = input("Tiro: ")
                    limpatela()
                    jogada = processa_jogada(tiro, navios)
                    if jogada == "":
                        tempo(3)
                    
                    atualizado = atualiza_tab(jogada, tab, frota)
                    if atualizado != "!" and jogada != "":
                        break


                

        def jogador_2(navios, tab, frota):
                while True:
                    limpatela()
                    print("           ----------- Jogador 2 ----------\n")
                    mostra_tabuleiro(tab)
                    print(f"Navios no mar: {len(navios)}\n")
                    tiro = input("Tiro: ")
                    limpatela()
                    jogada = processa_jogada(tiro, navios)
                    if jogada == "":
                        tempo(3)

                    atualizado = atualiza_tab(jogada, tab, frota)
                    if atualizado != "!" and jogada != "":
                        break
            
            
        tab_1, tab_2 = cria_tabuleiro(), cria_tabuleiro()
        navios_1, navios_2 = posiciona_navios()


        frota_1, frota_2 = copy.deepcopy(navios_1), copy.deepcopy(navios_2)
        print(f"{"-" * 37}\n         Modo dois jogadores\n{"-" * 37}\n")
        print("    Quem irá começar?\n\n(1) Jogador 1  (2) Jogador 2\n")
        jogador = input("Opção ")
        limpatela()


        if jogador == "1":
            while len(navios_1) != 0 and len(navios_2) != 0:
                jogador_1(navios_2, tab_2, frota_2)
                tempo(2)
                jogador_2(navios_1, tab_1, frota_1)
                tempo(2)

        elif jogador == "2":
            while len(navios_1) != 0 and len(navios_2) != 0:
                jogador_2(navios_1, tab_1, frota_1)
                tempo(2)
                jogador_1(navios_2, tab_2, frota_2)
                tempo(2)

        return navios_1, navios_2
    
    
    navios_1, navios_2 = jogo()
    if navios_1 > 0:
        print("   ============ O jogador 1 venceu ! ============")
        print("\nRealmente, ele é um marinheiro melhor que o jogador 2 !")
    else: 
        print("   ============ O jogador 2 venceu ! ============")
        print("\nRealmente, ele é um marinheiro melhor que o jogador 1 !")
    
        
    


def main():
     valor = True

     while valor: 
        limpatela()
        print("---------------------------------------\n             Batalha naval\n---------------------------------------\n")

        escolha = menu_incial()

        if escolha == "1":
            modo = modo_de_jogo()      
            limpatela()
            if modo == "1":
                modo_um_player()
            else:
                modo_dois_players()
            
            time.sleep(3)
            print("_" * 55)
            print("\nDeseja jogar novamente? (1) Sim  (2) Não\n")
                
            while True:
                resp = int(input("Opção: "))

                if resp == 1:
                    break
                elif resp == 2:
                    valor = False
                    break
                else:
                    print("\nDigite uma opção válida !")
        
        else:
            tutorial()


main()