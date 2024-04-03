'''
4. Crie  um  programa  que  funcione  com  base  em  laços  de  repetição,  onde  sempre  após executar uma tarefa ele irá voltar para a parte inicial até que seja pressionado “0”, além disso o mesmo deve receber a entrada de dois números inteiros que irão ser utilizados no programa, veja o exemplo a seguir:

    a. Saída/Impressão: 
        i. CALCULADORA:  
            1- somar  
            2- subtrair 
            3- multiplicar 
            0- sair  
            Insira sua opção: “1” 
        ii. Opcao - SOMAR  
            Insira o número desejado: “2”  
            Insira o próximo número: “2”  
            Resultado = 4 (voltando para o menu....)  
        iii. CALCULADORA:  
            1- somar  
            2- subtrair  
            3- multiplicar  
            0- sair
            Insira sua opção: “0”  
            Até logo!....
'''

menu = '''
1- somar  
2- subtrair 
3- multiplicar 
0- sair 
'''

while True:
    print(f'\n{menu}')
    opcao = int(input('Insira sua opção: '))
    if opcao == 0:
        print('Até logo!....')
        break
    elif opcao == 1:
        print('\nOpção - SOMAR')
        valor_a = float(input('Insira o número desejado: '))
        valor_b = float(input('Insira o próximo número: '))
        soma = valor_a + valor_b
        print(f'Resultado = {soma:.1f} (voltando para o menu....)')
    elif opcao == 2:
        print('\nOpção - SUBTRAIR')
        valor_a = float(input('Insira o número desejado: '))
        valor_b = float(input('Insira o próximo número: '))
        subtracao = valor_a - valor_b
        print(f'Resultado = {subtracao:.1f} (voltando para o menu....)')
    elif opcao == 3:
        print('\nOpção - MULTIPLICAR')
        valor_a = float(input('Insira o número desejado: '))
        valor_b = float(input('Insira o próximo número: '))
        multiplicacao = valor_a * valor_b
        print(f'Resultado = {multiplicacao:.1f} (voltando para o menu....)')
