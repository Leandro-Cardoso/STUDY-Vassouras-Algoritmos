'''
1. As Organizações PythonMaster resolveram dar um aumento de salário aos seus 
colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. 
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte 
critério, baseado no salário atual:

    o salários até R$ 280,00 (incluindo) : aumento de 20% 
    o salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
    o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
    o salários de R$ 1500,00 em diante : aumento de 5% 
    o Após o aumento ser realizado, informe na tela: o salário antes do reajuste; o 
    percentual de aumento aplicado; o valor do aumento; o novo salário, após o 
    aumento.
'''

def aumentar_salario(salario:float) -> dict:
    if salario <= 280:
        percentual = 0.2
    elif salario <= 700:
        percentual = 0.15
    elif salario <= 1500:
        percentual = 0.1
    else:
        percentual = 0.05

    aumento = salario * percentual
    novo_salario = salario + aumento

    return {
        'salario' : salario,
        'percentual' : percentual,
        'aumento' : aumento,
        'novo_salario' : novo_salario
    }

salario = float(input('Qual o salário do colaborador: '))
tabela = aumentar_salario(salario)

print(f'\nSalário antigo: R$ {tabela["salario"]:.2f}')
print(f'Percentual do aumento: {tabela["percentual"] * 100:.1f} %')
print(f'Valor do aumento: R$ {tabela["aumento"]:.2f}')
print(f'Novo salário: R$ {tabela["novo_salario"]:.2f}\n')
