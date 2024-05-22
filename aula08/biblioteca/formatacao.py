def formatar_dicionario(dicionario:dict) -> str:
    '''Formata um dicionário e retorna como string.'''
    barra = '=' * 58
    dicionario_formatado = f' {barra}\n'
    for i, chave in enumerate(list(dicionario)):
        i += 1
        valor = dicionario[chave]
        dicionario_formatado += f' | {i:>3} - {chave:^30} : {valor:>15} |\n'
    dicionario_formatado += f' {barra}'
    return dicionario_formatado

def formatar_menu(menu:list) -> str:
    '''Formata o menu e retorna como string.'''
    menu_formatado = ''
    for i, elemento in enumerate(menu):
        menu_formatado += f' {i + 1} - {elemento}'
        if i != len(menu) - 1:
            menu_formatado += '\n'
    return menu_formatado

def formatar_tela(titulo, informacoes = None, menu = None, erro = None) -> str:
    '''Formata a tela e retorna como string.'''
    titulo = str(titulo)
    titulo = titulo.upper()
    tela_formatada = f'\n {titulo}:\n'
    if informacoes != None:
        informacoes = str(informacoes)
        tela_formatada += f'\n{informacoes}\n'
    if menu != None:
        menu = str(menu)
        menu = menu.title()
        tela_formatada += f'\n{menu}\n'
    if erro != None:
        erro = str(erro)
        tela_formatada += f'\n <!> {erro} <!>\n'
    return tela_formatada
