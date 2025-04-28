''' -------------- !!! Atenção !!!-----------------
   
     A votação encerra quando você digita 999 na idade

'''


idade = 0 
cand = ["Jeferson Arantes do Nascimento", "Eduardo Ramires de Souza", "João Kleber Machado"]
votação = [{'Nome': cand[0], 'votos': 0},
           {'Nome': cand[1], 'votos': 0},
           {'Nome': cand[2], 'votos': 0}]


def Proximoeleitor(): 
              print("\n" * 2)
              print("-- Próximo eleitor --")
              print() #Pula linha


while idade != 999: #Se você pedir 999, a votação se encerrará e mostrará o resultado final
    
    
    idade = int(input("Informe sua idade: ")) 
    print() # Pula linha
    
    
    if idade < 15: print("Você não tem idade para votar!"), Proximoeleitor()
   
       
    elif idade == 999: 
        print("   -- Votação encerrada -- "), 
        print() #Pula linha  
        
         
            #Impressora de maior para menor voto:
        
        
        votação.sort(key= lambda candidato: candidato["votos"], reverse=True)
        for candidato in votação:
            print(candidato['Nome'], ": ", candidato['votos'], "votos")
           
       
    else:
        print("   -- Candidatos -- ")
        print() #Pula linha   
        print("{1} ", cand[0])
        print("{2} ", cand[1])
        print("{3} ", cand[2])
        print() #Pula linha
        
        
        num = int(input("Insira o número do candidato escolhido: "))
        
        
        while num < 1 or num > 3:
            num = int(input("Digite corretamente: "))  
        
        
        if num == 1: votação[0]['votos'] += 1
        elif num == 2: votação[1]['votos'] += 1
        elif num == 3: votação[2]['votos'] =+ 1
            
        
        print() #Pula linha
        print("Voto realizado com sucesso!")
        Proximoeleitor()
