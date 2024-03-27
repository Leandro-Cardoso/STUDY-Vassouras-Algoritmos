'''
1. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do 
arquivo usando este link (em minutos).
'''

# 1 byte = 8 bits

def tempo_download(tamanho:float, velocidade:float) -> float:
    velocidade_convertida = velocidade / 8
    estimativa = velocidade_convertida / 60
    return estimativa

tamanho = float(input('\nInforme o tamanho do arquivo em "MB": '))
velocidade = float(input('Informe a velocidade do link de internet em "Mbps": '))
resposta = tempo_download(tamanho, velocidade)

print(f'\nO download de {tamanho} MB, em {velocidade} Mbps terminará em aproximadamente {resposta:.4} minutos.\n')
