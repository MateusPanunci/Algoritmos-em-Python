import time
import os


def tempo(z):
      time.sleep(z)
      os.system('cls')


def limpatela():
      os.system('cls')


def real(num):
    num = round(num,2)
    num = str(num)
    
    intpart, decpart= num.split(".")
    decpart = zero(decpart)
    intpart = list(intpart)
    intpart = ponto(intpart)
    return f"R$ {intpart},{decpart}"
    
    #vírgula(sep)

def zero(dec):
    #Adiciona zero se apenas um dígito estiver presente
    if len(dec) == 1:
        dec += "0"
    return dec
  
    
def ponto(num):
    cont = 0
    newnum = ""
    
    
    # Verifica, de traz para frente, se deve colocar um ponto entre as casas
    for alg in num[-1:0:-1]: #Alg é lieralmente o valor da string
        cont = cont - 1
        if cont % -3 == 0:
            num[num.index(alg, cont)] = f".{alg}"
     
    
    for i in range(len(num)):
          newnum += num[i]
    return newnum


num = 1*10**23

while num > 1*10**16:
    limpatela()
    num = float(input("Insira um número: "))
    if num > 1*10**16:
        limpatela()
        print("O número deve ter no máximo 16 casas decimais à esquerda da vírgula !!!")
        tempo(5)

print(real(num))

#Ou
'''
num = float(input("Insira um número: "))
print(f"R$ {num:.2f}")
'''