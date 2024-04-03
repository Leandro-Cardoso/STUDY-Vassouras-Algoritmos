'''
2. Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for correta e false caso o contrário. Logo após elabore um “mini-sistema” de checar a senha inserida, onde  o  usuário  tem  3  tentativas  de  senha  e  caso  esse  número  seja  ultrapassado  o programa é encerrado. 
'''

def verificar_senha(senha:str) -> bool:
    senha_correta = 'Le1988'
    if senha == senha_correta:
        return True
    else:
        return False

tentativas = 3

for i in range(tentativas):
    senha = input('\nDigite sua senha: ')
    if verificar_senha(senha):
        print('\nSenha correta !!!\n')
        break
