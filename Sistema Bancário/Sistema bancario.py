import locale, os


opção, extrato, limite_saque, saque, saldo, ordem = 0, [], 0, 0, 0, 1
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def real(x):
      return locale.currency(x, grouping= True )


def limpatela():
      os.system('cls')

def voltar():
      print() #Pula linha
      input("Clique ENTER para voltar") 
      limpatela()


while opção != 4:
      limpatela()
      print("Saldo atual: ", real(saldo), "\n")
      print("O que deseja fazer?")
      print("{1} Sacar {2} Depositar {3} Extrato {4} Sair", '\n')
      opção = int(input("R: "))
      limpatela()
   

      if opção == 1:
           
            if saldo == 0:
                  print("Você não tem saldo para realizar essa operação !!!")
                  voltar()
         
           
            elif limite_saque < 3 and saldo > 0:
                  limite_saque += 1
                  print("Quanto você deseja sacar?")
                  saque = float(input("R$ "))
                  limpatela()
                  
                  if saque <= saldo:
                        
                        if saque > 500:
                              limite_saque -= 1
                              print("Você podê sacar até no máximo R$ 500,00 por vez !!!") 
                              voltar()
                        
                        
                        else:
                              extrato.append(f"{ordem}ª operação -> Saque: - {real(saque)}")
                              saque *= -1
                              saldo += saque
                              ordem += 1
                              print("Saque realizado com sucesso !!!")    
                              voltar()
                             
                  else:
                        limite_saque -= 1
                        print("Você não tem saldo sufuciente para sacar essa quantidade !!!")
                        voltar()
        
            else:
                  print("Você pode sacar apenas 3 vezes por mês !!!")
                  voltar()
                  
      elif opção == 2:
            print("Quanto você deseja depositar?")
            depósito = float(input("R$ "))
            saldo += depósito
            extrato.append(f"{ordem}ª operação -> Depósito: + {real(depósito)}")
            ordem += 1
            limpatela()
            print("Depósito realizado com sucesso !!!")   
            voltar()
   
      
      elif opção == 3: 
            print("Extrato:")
            for oper in extrato[::-1]: 
                  print(oper)
            voltar()
        
        
      elif opção == 4:
            print("Operação encerrada !!!")
           
  
      else:
            print("Opção inválida !!!")
            voltar()

         


    
      

 

