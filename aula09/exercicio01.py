'''
Tentar abrir um arquivo que não existe.
Se não existir crie um.
Use try e except.
Não pode usar "with".
'''

try:
    arquivo = open('exercicio01.txt', 'r')
    conteudo = arquivo.read()
    print(conteudo)
except:
    arquivo = open('exercicio01.txt', 'w')
    arquivo.write('Arquivo novo.')
finally:
    arquivo.close()
