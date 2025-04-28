def cria_triangulo(qtd_linhas):
    lista = []
  
  
    for i in range(0, qtd_linhas):
        linha = []
        if i == 0: #Primeira linha
          lista.append([1])
        
        elif i == 1: #Segunda linha
            for cont in range(2):
              linha.append(1)
            lista.append(linha)
          

        else: # Terceira em diante
            linha_anterior = lista[i-1] # indice da linha atual - 1
            linha.append(1)
            
          
            for posicao in range(0, len(linha_anterior)-1): #Soma os números da linha anterior até o penúltimo número dela
                proximo_num = linha_anterior[posicao + 1]
                num = linha_anterior[posicao] 
                
                
                soma = num + proximo_num
                linha.append(soma)
              
            
            linha.append(1) #Adiciona o 1 no final
            lista.append(linha)

            
    return lista


def mostra_triangulo(triangulo):
    print('')
    for linha in triangulo:
        for num in linha:
            print(num, end = ' ')
        print("")


if __name__ =='__main__':
    qtd_linhas = int(input("Insira a quantidade de linhas que você deseja imprimir do triângulo de pascal: "))
    triangulo = cria_triangulo(qtd_linhas)
    mostra_triangulo(triangulo)

 
       






  


     




