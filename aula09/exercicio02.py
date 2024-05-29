'''
Crie uma função que insira um dicionário em um arquivo de texto.
Deve ser salvo no arquivo:
chave1 : valor1
chave2 : valor2
chave3 : valor3
Utilize try e except.
'''

def salvar_dicionario(dicionario:dict) -> None:
    try:
        with open('exercicio02.txt', 'w', encoding = 'UTF-8') as arquivo:
            for chave in list(dicionario):
                arquivo.write(f'{chave} : {dicionario[chave]}\n')
    except Exception as e:
        print('Erro:', e)

dicionario = {
    'Leandro' : 35, 
    'Maria' : 24,
    'João' : 38
}

salvar_dicionario(dicionario)

with open('exercicio02.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(f'\n{conteudo}')
