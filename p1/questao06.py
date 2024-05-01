'''
6. Crie uma função que lê o ano de nascimento de uma pessoa e o ano atual. 
Calcule e mostre qual é: a idade da pessoa em anos, a idade da pessoa em meses, a idade da pessoa em dias e a idade da pessoa em semanas.
'''

def idade_anos(ano_nascimento:int, ano_atual:int) -> int:
    return ano_atual - ano_nascimento

def idade_meses(ano_nascimento:int, ano_atual:int) -> int:
    anos = idade_anos(ano_nascimento, ano_atual)
    return anos * 12

def idade_dias(ano_nascimento:int, ano_atual:int) -> int:
    anos = idade_anos(ano_nascimento, ano_atual)
    return anos * 365

def idade_semanas(ano_nascimento:int, ano_atual:int) -> int:
    dias = idade_dias(ano_nascimento, ano_atual)
    return dias / 7

ano_nascimento = 1988
ano_atual = 2024

anos = idade_anos(ano_nascimento, ano_atual)
meses = idade_meses(ano_nascimento, ano_atual)
dias = idade_dias(ano_nascimento, ano_atual)
semanas = idade_semanas(ano_nascimento, ano_atual)

print(f'''
    Anos: {anos}
    Meses: {meses}
    Dias: {dias}
    Semanas: {semanas:.1f}
    ''')
