def linha():
    print("_" * 150, "\n" )

def conteudo_inicial(arq):
    linha()
    print("---- Cadastro de Mercadorias ----\n")
    print("Observações:\n. Insira as mercadorias da dispensa no seguinte formato: código da mercadoria, descrição, quantidade atual.")
    print(". Os códigos devem seguir a sequência 101,102,103...\n. Ex: 101, Arroz, 50\n. Se não desejar colocar mais mercadorias, só pressione enter\n ")
    while True:
        frase = input("")
        if frase == "":
            break


        print(frase, file = arq)
  
def main():
   with open("mercadorias.txt", "w") as arq:
        conteudo_inicial(arq)

   while True:
        arq = open("mercadorias.txt", "r") 
        linha()
        arq.seek(0)
        print(" ---- Gerenciador de mercadorias ----\n")   
        print("(1) Adicionar ou retirar mercadorias\n(2) Fazer um relátório\n(3) Sair\n")
   
        resp = input("Opção ")

        if resp == "1":
              linha()
              print("---- Adição/retirada de produtos ----")
              print("\n(1) Adicionar\n(2) Retirar\n")
              while True:
                  resp2 = input("Opção ")
                

                  if resp2 == "1": #Adicionar
                      linha()
                      while True:
                          arq.seek(0)
                          print("Qual é o código do produto?")
                          codigo = input("R: ")
                          print("\nQuantos unidades deseja adicionar?")
                          qtd = int(input("R: "))
                          
                          linhas, cont = arq.readlines(), 0

                          for i, line in enumerate(linhas):
                              codigo_line, nome, num = line.strip().split(",")
                              if codigo == codigo_line:
                                  num = int(num)
                                  new_num = num + qtd
                                  cont += 1


                                  if new_num < 0:
                                    new_num = 0

                                  linhas[i] = f"{codigo_line},{nome}, {new_num}\n"
                            
                          
                          if cont > 0:
                              with open("mercadorias.txt", "w") as arq:
                                  arq.writelines(linhas)
                              print("\nUnidades adicionadas com sucesso!")
                              break
                        
                        
                          else:
                              print("\nVocê não digitou uma opção existente, tente novamente!\n")
                              continue 
                        

                  elif resp2 == "2": #Retirar
                      linha()
                      while True:
                          arq.seek(0)
                          print("Qual é o código do produto?")
                          codigo = input("R: ")
                          print("\nQuantas unidades deseja retirar?")
                          qtd = int(input("R: "))
                            

                          linhas = arq.readlines()
                          cont = 0

                          for i, line in enumerate(linhas):
                              codigo_line, nome, num = line.strip().split(",")
                              if codigo == codigo_line:
                                  cont += 1
                                  print(cont)
                                  num = int(num)
                                  new_num = num - qtd

                                  if new_num < 0:
                                    new_num = 0
    
                                  linhas[i] = f"{codigo_line},{nome}, {new_num}\n"
                                               
                          
                          if cont > 0:
                              with open("mercadorias.txt", "w") as arq:
                                  arq.writelines(linhas)
                              print("\nUnidades retiradas com sucesso!")
                              break


                          else:
                              print("\nVocê não digitou uma opção existente, tente novamente!\n")
                              continue 

              
                  else: #Digitar novamente
                      print("\nVocê não digitou uma opção existente, tente novamente!\n")
                      continue 


                  break
                  
                
        elif resp == "2":
              linha()
              print("---- Relatórios ----\n")
              print("(1) Relatório Geral (2) Produtos não disponíveis\n")
              while True:
                  resp2 = input("Opção ")
                  if resp2 == "1": #Relatório geral
                      linha()
                      print("---- Situação atual dos produtos ----")
                      print(f"\n{arq.read()}")
     
                  elif resp2 == "2": # Zero unidades
                      cont_lines = 0
                      
                      linha()
                      print("---- Produtos não disponíveis ----\n")
                      for line in arq:
                           codigo_line, nome, num = line.strip().split(",")
                           if int(num) == 0 :
                               print(f"{codigo_line} -{nome}")
                               cont_lines += 1

                        
                      if cont_lines == 0:
                           print("\nHá unidades para todas as mercadorias!")
                     

                  else:
                      print("\nVocê não digitou um código de produto existente, tente novamente!\n")
                      continue
        
                  break
       
       
        elif resp == "3":
              print("\nPrograma encerrado!")
              break
             

main()
       
