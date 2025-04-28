import os, time


def limpatela():
    os.system('cls')


def tempo(z):
    time.sleep(z)
    limpatela()


def tutorial():
    print("   ------ Tutorial ------\n")
    print(". No jogo da velha, um jogador vence se conseguir preencher três posições consecutivas (horizontalmente, verticalmente ou diagonalmente).")
    print(". O jogador número 1 será o símbolo \"O\" e o jogador número 2 o \"X\".")
    print(". Para preencher uma posição, digite um número de 1 a 9, de acordo com a figura abaixo:\n")
    print(f"{" " * 21}{1}  |   {2}   |  {3}")
    print(f"{" " * 18}------+-------+------")
    print(f"{" " * 21}{4}  |   {5}   |  {6}")
    print(f"{" " * 18}------+-------+------")
    print(f"{" " * 21}{7}  |   {8}   |  {9}\n")
    input("Clique ENTER para voltar para o menu")
    limpatela()


def mostra_jogo(jogo):
    print(f"{" " * 21}{jogo[0][0]}  |   {jogo[0][1]}   |  {jogo[0][2]}")
    print(f"{" " * 18}------+-------+------")
    print(f"{" " * 21}{jogo[1][0]}  |   {jogo[1][1]}   |  {jogo[1][2]}")
    print(f"{" " * 18}------+-------+------")
    print(f"{" " * 21}{jogo[2][0]}  |   {jogo[2][1]}   |  {jogo[2][2]}\n")


def cria_jogo():
    jogo = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
    ]
    
    return jogo

def processa_jogada(jogada, jogo):
    try:
        if jogada == "1":
             jogada_lista = [0,0]
        elif jogada == "2":
             jogada_lista = [0,1]
        elif jogada == "3":
             jogada_lista = [0,2]
        elif jogada == "4":
             jogada_lista = [1,0]
        elif jogada == "5":
             jogada_lista = [1,1]
        elif jogada == "6":
             jogada_lista = [1,2]
        elif jogada == "7":
             jogada_lista = [2,0]
        elif jogada == "8":
             jogada_lista = [2,1]
        elif jogada == "9":
             jogada_lista = [2,2]
        else:
             raise
        
    
        # Se a letra for diferente das do tabuleiro
        if jogada_lista[0] > 2 or jogada_lista[1] > 2 or jogada_lista[0] < 0 or jogada_lista[1] < 0:
            raise
        

        if len(jogada_lista) > 2 or len(jogada_lista) < 0:
            raise

        return jogada_lista


    except BaseException:
        print("Você digitou a posição pretendida de maneira incorreta, tente novamente!")
        return "!"
    
def atualiza_jogo(jogador, jogada, jogo):
    if jogo[jogada[0]][jogada[1]] != "X" and jogo[jogada[0]][jogada[1]] != "O":
        if jogador == 1:
            jogo[jogada[0]][jogada[1]] = "O"
        else:
            jogo[jogada[0]][jogada[1]] = "X"
    else:
        print("Esta posição já foi utilizada, tente novamente!")
        return "!"
        


def verifica_win(jogo):
    cont = 0
    while cont < 3:
        if jogo[cont] == ["X", "X", "X"]:
            return "X"
        elif jogo[cont] == ["O", "O", "O"]:
            return "O"
              
        cont += 1
    

    for j in range(0, 3):
        column = [jogo[i][j] for i in range(0, 3)] 
        if column == ["X", "X", "X"]:
            return "X"
        
        elif column == ["O", "O", "O"]:
            return "O"


    diagonal, cont = [], 2
    while cont > 0:
        if cont == 1:
            diagonal_1 = [jogo[l][l] for l in range(0,3)]
            
            if diagonal_1 == ["X", "X", "X"]:
                return "X"
            elif diagonal_1 == ["O", "O", "O"]:
                return "O"
        else:
            diagonal_2, m = [], -1
            for l in range(0,3):
                diagonal_2.append(jogo[l][m])
                m -= 1


            if diagonal_2 == ["X", "X", "X"]:
                return "X"
                  
            elif diagonal_2 == ["O", "O", "O"]:
                return "O"
        
        cont -= 1
    
        
    return ""
   

def jogo():
    while True:
        jogo = cria_jogo()
        num_jogadas, vence = 0, ""
        while num_jogadas < 9:
            limpatela()
            if num_jogadas % 2 == 0:
                i = 1
            else:
                i = 2
            print(f"                 -----  Jogador {i}  -----\n")
            mostra_jogo(jogo)
            while True:
                jogada = input("\nPosição: ")
                processada = processa_jogada(jogada, jogo)
                if processada == "!":
                    continue
                else:
                    atualizado = atualiza_jogo(i, processada, jogo)
                    if atualizado == "!":
                        continue
                    else:
                        break
            
            verificado = verifica_win(jogo)
            if verificado == "X":
                limpatela()
                print("   ============ O jogador 2 venceu ! ============")
                print("\n          Cara é craque no jogo da velha !")
                vence = "Ok"
                break
            
            elif verificado == "O":
                limpatela()
                print("   ============ O jogador 1 venceu ! ============")
                print("\n           Cara é brabo no jogo da velha !")
                vence = "Ok"
                break

            
            num_jogadas += 1

        
        if vence == "":
            limpatela()
            print("   --------- Empate ---------\n")
            print('   A velha ganhou essa partida')

        
        time.sleep(3)
        print("_" * 55)
        print("\n   Selecione uma das opções:")
        print("\n(1) Jogar novamente  (2) Voltar para o menu  (3) Sair do jogo \n")
            
        while True:
            resp = input("Opção: ")

            if resp == "1":
                break
            elif resp == "2":
                limpatela()
                return ""
            
            elif resp == "3":
                valor = False
                return valor
            else:
                print("\nDigite uma opção válida !")


     
def main():
    valor = True
    while valor:
        print(f"{"-"*30}\n         JOGO DA VELHA\n{"-"*30}\n")
        print("  (1) Jogar     (2) Tutorial\n\n")
        while True:
            resp = input("Opção: ")

            if resp == "1":
                encerra = jogo()
                if encerra == False:
                    limpatela()
                    print("Jogo encerrado !")
                    valor = False 
                break
                
            elif resp == "2":
                limpatela()
                tutorial()
                break

            else:
                print("\nDigite uma opção válida !")


main()
   
