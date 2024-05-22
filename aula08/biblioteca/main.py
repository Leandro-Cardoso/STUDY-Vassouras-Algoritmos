from os import system

from config import USUARIO_ADMIN, SENHA_ADMIN
from formatacao import formatar_tela, formatar_menu, formatar_dicionario
from gerenciamento import somar_dicionarios, subtrair_dicionarios, buscar_dicionario

def buscar_usuario(usuarios:dict) -> None:
    '''Exibe o resultado da busca de um usuário.'''
    titulo = 'buscar usuário'
    tela = formatar_tela(titulo = titulo)
    system('cls')
    print(tela)
    usuario = input(' Usuário: ')
    usuario = buscar_dicionario(usuarios, usuario)
    if usuario == {}:
        informacoes = None
        erro = 'Nenhum resultado encontrado...'
    else:
        erro = None
        informacoes = formatar_dicionario(usuario)
    opcoes = ['sair']
    menu = formatar_menu(opcoes)
    while True:
        tela = formatar_tela(titulo = titulo, informacoes = informacoes, menu = menu, erro = erro)
        erro = None
        system('cls')
        print(tela)
        opcao = input(' Opção: ')
        if opcao == '1':
            break
        else:
            erro = 'Opção inválida! Digite o número referente a opção desejada.'

def listar_usuarios(usuarios:dict) -> None:
    '''Exibe uma lista com todos os usuários cadastrados.'''
    titulo = 'listar usuários'
    if len(list(usuarios)) < 1:
        informacoes = ' Nenhum usuário cadastrado...'
    else:
        informacoes = formatar_dicionario(usuarios)
    opcoes = ['sair']
    menu = formatar_menu(opcoes)
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, informacoes = informacoes, menu = menu, erro = erro)
        erro = None
        system('cls')
        print(tela)
        opcao = input(' Opção: ')
        if opcao == '1':
            break
        else:
            erro = 'Opção inválida! Digite o número referente a opção desejada.'

def alterar_senha(usuarios:dict) -> dict:
    '''Altera a senha de um usuário cadastrado.'''
    titulo = 'alterar senha'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        usuario = input(' Usuário: ')
        senha = input(' Nova senha: ')
        if usuario in list(usuarios):
            usuarios.update({usuario : senha})
            break
        else:
            erro = 'Não existe cadastro desse usuário.'
    return usuarios

def remover_usuario(usuarios:dict) -> dict:
    '''Remove um usuário cadastrado.'''
    titulo = 'remover usuário'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        usuario = input(' Usuário: ')
        if usuario == USUARIO_ADMIN:
            erro = 'O usuário administrador não pode ser removido.'
        elif usuario in list(usuarios):
            usuario = buscar_dicionario(usuarios, usuario)
            usuarios = subtrair_dicionarios(usuarios, usuario)
            break
        else:
            erro = 'Não existe cadastro desse usuário.'
    return usuarios

def cadastrar_usuario(usuarios:dict) -> dict:
    '''Cadastra um novo usuário.'''
    titulo = 'cadastrar usuário'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        usuario = input(' Usuário: ')
        senha = input(' Senha: ')
        if usuario not in list(usuarios):
            novo_usuario = {usuario : senha}
            usuarios = somar_dicionarios(usuarios, novo_usuario)
            break
        else:
            erro = 'Já existe cadastro desse usuário.'
    return usuarios

def gerenciar_usuarios(usuarios:dict) -> dict:
    '''Tela de gerenciamento de usuários (Apenas o Admin tem acesso).'''
    titulo = 'gerenciar usuários'
    opcoes = ['sair' ,'cadastrar usuário', 'remover usuário', 'alterar senha', 'listar usuários', 'buscar usuário']
    menu = formatar_menu(opcoes)
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, menu = menu, erro = erro)
        erro = None
        system('cls')
        print(tela)
        opcao = input(' Opção: ')
        if opcao == '1':
            break
        elif opcao == '2':
            usuarios = cadastrar_usuario(usuarios)
        elif opcao == '3':
            usuarios = remover_usuario(usuarios)
        elif opcao == '4':
            usuarios = alterar_senha(usuarios)
        elif opcao == '5':
            listar_usuarios(usuarios)
        elif opcao == '6':
            buscar_usuario(usuarios)
        else:
            erro = 'Opção inválida! Digite o número referente a opção desejada.'
    return usuarios

def listar_reservados(reservados:dict) -> None:
    '''Exibe uma lista com todos os livros reservados.'''
    titulo = 'listar reservados'
    if len(list(reservados)) < 1:
        informacoes = ' Nenhum livro reservado...'
    else:
        informacoes = formatar_dicionario(reservados)
    opcoes = ['sair']
    menu = formatar_menu(opcoes)
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, informacoes = informacoes, menu = menu, erro = erro)
        erro = None
        system('cls')
        print(tela)
        opcao = input(' Opção: ')
        if opcao == '1':
            break
        else:
            erro = 'Opção inválida! Digite o número referente a opção desejada.'

def devolver_livro(livros:dict, reservados:dict) -> dict:
    '''Faz a devolução de um livro reservado.'''
    titulo = 'devolver livro'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        titulo_livro = input(' Livro: ')
        titulo_livro = titulo_livro.title()
        livro = buscar_dicionario(reservados, titulo_livro)
        if livro == {}:
            erro = 'Nenhum resultado encontrado...'
        else:
            livro[titulo_livro] = 1
            reservados = subtrair_dicionarios(reservados, livro)
            livros = somar_dicionarios(livros, livro)
            return livros, reservados

def reservar_livro(livros:dict, reservados:dict) -> dict:
    '''Faz reserva de um livro que esteja disponível.'''
    titulo = 'reservar livro'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        titulo_livro = input(' Livro: ')
        titulo_livro = titulo_livro.title()
        livro = buscar_dicionario(livros, titulo_livro)
        if livro == {}:
            erro = 'Nenhum resultado encontrado...'
        else:
            livro[titulo_livro] = 1
            livros = subtrair_dicionarios(livros, livro)
            reservados = somar_dicionarios(reservados, livro)
            return livros, reservados

def buscar_livro(livros:dict) -> None:
    '''Exibe o resultado da busca de um livro.'''
    titulo = 'buscar livro'
    tela = formatar_tela(titulo = titulo)
    system('cls')
    print(tela)
    alvo = input(' Livro: ')
    alvo = alvo.title()
    alvo = buscar_dicionario(livros, alvo)
    if alvo == {}:
        informacoes = None
        erro = 'Nenhum resultado encontrado...'
    else:
        erro = None
        informacoes = formatar_dicionario(alvo)
    opcoes = ['sair']
    menu = formatar_menu(opcoes)
    while True:
        tela = formatar_tela(titulo = titulo, informacoes = informacoes, menu = menu, erro = erro)
        erro = None
        system('cls')
        print(tela)
        opcao = input(' Opção: ')
        if opcao == '1':
            break
        else:
            erro = 'Opção inválida! Digite o número referente a opção desejada.'

def listar_livros(livros:dict) -> None:
    '''Exibe uma lista com todos os livros disponiveis.'''
    titulo = 'listar livros'
    if len(list(livros)) < 1:
        informacoes = ' Nenhum livro disponível...'
    else:
        informacoes = formatar_dicionario(livros)
    opcoes = ['sair']
    menu = formatar_menu(opcoes)
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, informacoes = informacoes, menu = menu, erro = erro)
        erro = None
        system('cls')
        print(tela)
        opcao = input(' Opção: ')
        if opcao == '1':
            break
        else:
            erro = 'Opção inválida! Digite o número referente a opção desejada.'

def remover_livros(livros:dict) -> dict:
    '''Remove livros disponíveis e retorna um novo dicionário.'''
    titulo = 'remover livros'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        livro = input(' Livro: ')
        livro = livro.title()
        quantidade = input(' Quantidade: ')
        try:
            quantidade = int(quantidade)
            livro_removido = {livro : quantidade}
            livros = subtrair_dicionarios(livros, livro_removido)
            break
        except:
            erro = 'Valor inválido! A quantidade precisa ser um número inteiro.'
    return livros

def registrar_livros(livros:dict) -> dict:
    '''Registra novos livros e retorna um novo dicionário.'''
    titulo = 'registrar livros'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        livro = input(' Livro: ')
        livro = livro.title()
        quantidade = input(' Quantidade: ')
        try:
            quantidade = int(quantidade)
            novo_livro = {livro : quantidade}
            livros = somar_dicionarios(livros, novo_livro)
            break
        except:
            erro = 'Valor inválido! A quantidade precisa ser um número inteiro.'
    return livros

def login(usuarios:dict) -> str:
    '''Tela de login. Retorna o nome de usuario logado.'''
    titulo = 'login'
    erro = None
    while True:
        tela = formatar_tela(titulo = titulo, erro = erro)
        erro = None
        system('cls')
        print(tela)
        usuario = input(' Usuário: ')
        senha = input(' Senha: ')
        if usuario in list(usuarios) and usuarios[usuario] == senha:
                return usuario
        else:
            erro = 'Usuário ou senha incorretos.'

def main() -> None:
    usuarios = {USUARIO_ADMIN : SENHA_ADMIN}
    livros = {}
    reservados = {}
    usuario_logado = login(usuarios)
    titulo = 'biblioteca'
    erro = None
    while True:
        opcoes = ['sair' ,'relogar', 'registrar livros', 'remover livros', 'listar livros', 'buscar livro', 'reservar livro', 'devolver livro', 'listar reservados']
        if usuario_logado == USUARIO_ADMIN:
            opcoes.append('gerenciar usuários (admin)')
        menu = formatar_menu(opcoes)
        tela = formatar_tela(titulo = titulo, menu = menu, erro = erro)
        erro = None
        system('cls')
        print(tela)
        opcao = input(' Opção: ')
        if opcao == '1':
            break
        elif opcao == '2':
            usuario_logado = login(usuarios)
        elif opcao == '3':
            livros = registrar_livros(livros)
        elif opcao == '4':
            livros = remover_livros(livros)
        elif opcao == '5':
            listar_livros(livros)
        elif opcao == '6':
            buscar_livro(livros)
        elif opcao == '7':
            livros, reservados = reservar_livro(livros, reservados)
        elif opcao == '8':
            livros, reservados = devolver_livro(livros, reservados)
        elif opcao == '9':
            listar_reservados(reservados)
        elif opcao == '10' and usuario_logado == USUARIO_ADMIN:
            usuarios = gerenciar_usuarios(usuarios)
        else:
            erro = 'Opção inválida! Digite o número referente a opção desejada.'
    system('cls')
    print('\nVolte sempre !!!\n')

if __name__ == '__main__':
    main()
