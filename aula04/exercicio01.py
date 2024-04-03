'''
1. Crie 2 listas: uma com 5 nomes(João, Maria, Kleber, Caio e Sarah) e outra com 5 valores em  reais(R$)  correspondentes  ao  saldo  da  conta  do  usuário(1350,20;  240,50;  30,00; 830,15  e  50,00),  e  usando  laços  de  repetição  imprima  os  dados  da  seguinte  forma(o preenchimento das listas deve ser feito também com laços de repetição do mesmo modo que será impresso: salvar nome e depois salvar o saldo correspondente): 

    Entradas:  
    Insira o nome: ****  
    Insira o saldo: **** 
    
    Saída/Impressão:  
    LISTA DE CLIENTES - BANCO NACIONAL  
    NOME         SALDO          CONTA  
    nome0        saldo0         #0  
    nome1        saldo1         #2  
    nome2        saldo2         #4
'''

nomes = []
saldos = []
n = 5

print('\nEntradas:')
for i in range(n):
    nome = input('\nInsira o nome: ')
    saldo = float(input('Insira o saldo: '))
    nomes.append(nome)
    saldos.append(saldo)

col = 15
print('\nSaída/Impressão:')
print('\nLISTA DE CLIENTES - BANCO NACIONAL')
print('NOME' + (col - 4) * ' ' + 'SALDO' + (col - 5) * ' ' + 'CONTA')

for i in range(n):
    print(nomes[i] + (col - len(nomes[i])) * ' ' + str(saldos[i]) + (col - len(str(saldos[i]))) * ' ' + '#' + str(i))
print('\n')
