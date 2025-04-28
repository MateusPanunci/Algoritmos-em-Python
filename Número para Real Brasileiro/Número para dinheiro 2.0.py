import os


def formata_num_para_real(num):
    num_formatado = f"R$ {num:,.2f}"# Formata o número com duas casas decimais e vírgulas como separador de milhar
    return num_formatado.replace(",","X").replace(".",",").replace("X",".")
    

num = float(input("Insira um número: "))
print(formata_num_para_real(num))