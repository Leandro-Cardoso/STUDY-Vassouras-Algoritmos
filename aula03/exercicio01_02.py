'''
2. Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que 
são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça
um programa que nos dê:

    • salário bruto.
    • quanto pagou ao INSS.
    • quanto pagou ao sindicato.
    • salário líquido.
    • calcule os descontos e o salário líquido, conforme a tabela abaixo:
    
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
'''

def salario_mensal(ganho_hora:float, horas_trabalhadas:float) -> dict:
    salario_mes = ganho_hora * horas_trabalhadas
    ir = salario_mes * 0.11
    inss = salario_mes * 0.08
    sindicato = salario_mes * 0.05
    salario_liquido = salario_mes - ir - inss - sindicato
    return {
        'salario_mes' : salario_mes,
        'ir' : ir,
        'inss' : inss,
        'sindicato' : sindicato,
        'salario_liquido' : salario_liquido
    }

ganho_hora = float(input('\nQuando você ganha por hora: '))
horas_trabalhadas = float(input('Quantas horas você trabalhou no mês: '))

tabela = salario_mensal(ganho_hora, horas_trabalhadas)

print(f'\n + Salário do mês: R$ {tabela["salario_mes"]:.2f}')
print(f' - IR: R$ {tabela["ir"]:.2f}')
print(f' - INSS: R$ {tabela["inss"]:.2f}')
print(f' - Sindicato: R$ {tabela["sindicato"]:.2f}')
print(f' = Salário Liquido: R$ {tabela["salario_liquido"]:.2f}\n')
