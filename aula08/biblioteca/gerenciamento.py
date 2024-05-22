def buscar_dicionario(dicionario:dict, alvo:str) -> dict:
    '''Buscar um dicionário e retorna-lo.'''
    lista = list(dicionario)
    lista.sort()
    inicio = 0
    fim = len(lista) - 1
    while fim != 0:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return {alvo : dicionario[alvo]}
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return {}

def subtrair_dicionarios(dicionario_1:dict, dicionario_2:dict) -> dict:
    '''Subtrai dois dicionários e retorna um novo dicionário.'''
    for chave in list(dicionario_2):
        if chave in list(dicionario_1):
            if type(dicionario_1[chave]) == int or type(dicionario_1[chave]) == float:
                dicionario_1[chave] -= dicionario_2[chave]
                if dicionario_1[chave] <= 0:
                    del dicionario_1[chave]
            else:
                del dicionario_1[chave]
    return dicionario_1

def somar_dicionarios(dicionario_1:dict, dicionario_2:dict) -> dict:
    '''Soma dois dicionários e retorna um novo dicionário.'''
    for chave in list(dicionario_2):
        if chave in list(dicionario_1):
            dicionario_1[chave] += dicionario_2[chave]
        else:
            dicionario_1.update({chave : dicionario_2[chave]})
    return dicionario_1
