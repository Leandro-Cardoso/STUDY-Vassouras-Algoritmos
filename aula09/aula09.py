'''
AULA 09:

- Leitura e escrita de arquivos.
- Criação de log.
- Exceções (erros).
    - try, except, finally.
    - raise.
'''

# LER:
with open('aula09.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# CRIAR E ESCREVER OU REESCREVE:
with open('aula092.txt', 'w') as arquivo:
    arquivo.write('Ola, mundo !!!')

# CRIAR OU ACRESCENTAR:
with open('aula092.txt', 'a') as arquivo:
    arquivo.write('\nMais uma linha.')

# try, except, finally:
try:
    a = 10 / 0
    print(a)
except Exception as e:
    print(f'Erro: {e}')
finally:
    print('Essa sempre aparece.')
