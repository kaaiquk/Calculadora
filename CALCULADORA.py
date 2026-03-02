import time
while True:
    print('-'*21)
    print('\033[41mCalculadora em python\033[m')
    print('-'*21)
    time.sleep(0.3)
    print('''Escolha uma das operações
\033[32m[ 1 ]\033[m Adição
\033[32m[ 2 ]\033[m Subtração
\033[32m[ 3 ]\033[m Multiplicação
\033[32m[ 4 ]\033[m Divisão
\033[32m[ 5 ]\033[m Exponenciação
\033[31m[ 6 ]\033[m SAIR''')
    escolha=int(input('Digite um número: '))
    if escolha==6:
        break
    elif escolha==1:
        num1=int(input('Digite o primeiro número da soma: '))
        num2=int(input('Digite o segundo número da soma: '))
        soma=num1+num2
        print(f'O resultado dá \033[33m{soma}\033[m.')
        time.sleep(2)
    elif escolha==2:
        num1=int(input('Digite o primeiro número da subtração: '))
        num2=int(input('Digite o segundo número da subtração: '))
        subtração=num1-num2
        print(f'O resultado dá \033[33m{subtração}\033[m.')
        time.sleep(2)
    elif escolha==3:
        num1=int(input('Digite o primeiro fator da multiplicação: '))
        num2=int(input('Digite o segundo fator da multiplicação: '))
        multiplicação=num1*num2
        print(f'O produto dá \033[33m{multiplicação}\033[m.')
        time.sleep(2)
    elif escolha==4:
        num1=int(input('Digite o dividendo da divisão: '))
        num2=int(input('Digite o divisor da divisão: '))
        divisão=num1/num2
        print(f'O quociente dá \033[33m{divisão:.1f}\033[m')
        time.sleep(2)
    elif escolha==5:
        num1=int(input('Digite um número para ser exponencionado: '))
        num2=int(input('Digite o expoente: '))
        exponenciação=num1**num2
        print(f'A potência dá \033[33m{exponenciação}\033[m.')
        time.sleep(2)
    else:
        print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
        time.sleep(1)
print('\033[31mSAINDO DO PROGRAMA\033[m')
    
    