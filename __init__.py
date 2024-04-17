from random import choice, randint
from platform import system as platform_system
from os import system
from time import sleep

#declarar listas
caracteres_especiais = ('!', '@', '#', '$', '%', '&', '*', '/')
letras_maiusculas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
letras_minusculas = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
letras_maiusculas_minusculas = ('Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz')
num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

senha = []

#Funções

#Senhas Simples
def senha_simples_numeros():
    for c in range(0, x):
        senha.append(choice(num))

def senha_simples_letras_maiusculas():
    for c in range(0, x):
        senha.append(choice(letras_maiusculas))

def senha_simples_letras_minusculas():
    for c in range(0, x):
        senha.append(choice(letras_minusculas))

#Senhas Compostas
def senhas_compostas_letras_maiusculas_minusculas():
    for c in range(0, x):
        separacao = list(letras_maiusculas_minusculas[randint(0, 25)])
        senha.append(separacao[randint(0,1)])

def senha_compostas_letras_maiusculas_numeros():
    for c in range(0, x):
        aleatorio = randint(0,1)
        if aleatorio == 0:
            senha.append(letras_maiusculas[randint(0, 25)])
        elif aleatorio == 1:
            senha.append(num[randint(0, 9)])

def senha_compostas_letras_minusculas_numeros():
    for c in range(0, x):
        aleatorio = randint(0,1)
        if aleatorio == 0:
            senha.append(letras_minusculas[randint(0, 25)])
        elif aleatorio == 1:
            senha.append(num[randint(0, 9)])

#Senha Forte
def senha_forte():
    for c in range(0, x):
        aleatorio = randint(0, 2)
        if aleatorio == 0:
            separacao = list(letras_maiusculas_minusculas[randint(0, 25)])
            senha.append(separacao[randint(0,1)])
        elif aleatorio == 1:
            senha.append(num[randint(0, 9)])
        elif aleatorio == 2:
            senha.append(caracteres_especiais[randint(0, 7)])

#Funções Adicionais
def limpar_senha():
    senha.clear()

def identificar_sistema_operacional():
    sistema = platform_system()
    if sistema == "Windows":
        return "Windows"
    elif sistema == "Darwin":
        return "Mac"
    elif sistema == "Linux":
        return "Linux"
    else:
        return "Sistema não identificado"

def sistema_operacional_if():
    if sistema_operacional == 'Windows':
        return system('cls')
    elif sistema_operacional == 'Linux' or sistema_operacional == 'Mac':
        return system('clear')
    
sistema_operacional = identificar_sistema_operacional()

#Código
while True:
    x = int(input('Quantos digitos você quer na sua senha? (recomendado: 15) --> '))
    sistema_operacional_if()

    opcao_de_senha = str(input("""Qual tipo de senha você quer?

[1] Senha Simples:
    • Números
    • Letras Maiúsculas
    • Letras Minúsculas

[2] Senha Composta:
    • Letras Maiúsculas e Minúsculas
    • Letras Maiúsculas com Números
    • Letras Mínusculas com Números

[3] Senha Forte:
    • Letras Maiúsculas, Minúsculas, Números e Carateres Especiais

Escolha (1, 2, 3): """)).strip().upper()
    sistema_operacional_if()

    if opcao_de_senha == '1' or opcao_de_senha == 'SENHA SIMPLES':
        opcao_de_modo = str(input("""SENHA SIMPLES

[1] Números
[2] Letras Maiúsculas
[3] Letras Minúscula

Escolha (1, 2, 3): """)).strip().upper()
        sistema_operacional_if()
        if opcao_de_modo == '1' or opcao_de_modo == 'NÚMEROS' or opcao_de_modo == 'NUMEROS':
            print('\nSenhas')
            for c in range(0, 5):
                sleep(0.5)
                senha_simples_numeros()
                separador = ''
                print(f'\n{separador.join(senha)}')
                limpar_senha()

        elif opcao_de_modo == '2' or opcao_de_modo == 'LETRAS MAIÚSCULAS' or opcao_de_modo == 'LETRAS MAIUSCULAS':  
            print('\nSenhas')
            for c in range(0, 5):
                sleep(0.5)
                senha_simples_letras_maiusculas()
                separador = ''
                print(f'\n{separador.join(senha)}')
                limpar_senha()

        elif opcao_de_modo == '3' or opcao_de_modo == 'LETRAS MINÚSCULAS' or opcao_de_modo == 'LETRAS MINUSCULAS':  
            print('\nSenhas')
            for c in range(0, 5):
                sleep(0.5)
                senha_simples_letras_minusculas()
                separador = ''
                print(f'\n{separador.join(senha)}')
                limpar_senha()

    elif opcao_de_senha == '2' or opcao_de_senha == 'SENHA COMPOSTA':
        opcao_de_modo = str(input("""SENHA COMPOSTA

[1] Letras Maiúsculas e Minúsculas
[2] Letras Maiúsculas com Números
[3] Letras Mínusculas com Números

Escolha (1, 2, 3): """)).strip().upper()
        sistema_operacional_if()
        if opcao_de_modo == '1' or opcao_de_modo == 'LETRAS MAIÚSCULAS E MINÚSCULAS' or opcao_de_modo == 'LETRAS MAIUSCULAS E MINUSCULAS':
            print('\nSenhas')
            for c in range(0, 5):
                sleep(0.5)
                senhas_compostas_letras_maiusculas_minusculas()
                separador = ''
                print(f'\n{separador.join(senha)}')
                limpar_senha()

        elif opcao_de_modo == '2' or opcao_de_modo == 'LETRAS MAIÚSCULAS COM NÚMEROS' or opcao_de_modo == 'LETRAS MAIUSCULAS COM NUMEROS':
            print('\nSenhas')
            for c in range(0, 5):
                sleep(0.5)
                senha_compostas_letras_maiusculas_numeros()
                separador = ''
                print(f'\n{separador.join(senha)}')
                limpar_senha()

        elif opcao_de_modo == '3' or opcao_de_modo == 'LETRAS MINÚSCULAS COM NÚMEROS' or opcao_de_modo == 'LETRAS MINUSCULAS COM NUMEROS':
            print('\nSenhas')
            for c in range(0, 5):
                sleep(0.5)
                senha_compostas_letras_minusculas_numeros()
                separador = ''
                print(f'\n{separador.join(senha)}')
                limpar_senha()

    elif opcao_de_senha == '3' or opcao_de_senha == 'SENHA FORTE':
        print('\nSenhas')  
        for c in range(0, 5):
            sleep(0.5)
            senha_forte()
            separador = ''
            print(f'\n{separador.join(senha)}')
            limpar_senha()
        
    else:
        print('\nOpção inválida')
    
    sleep(1)
    pergunta = str(input("""
Executar código novamente?

[1] Sim
[2] Não
                         
Escolha: """)).strip().upper()
    if pergunta == '1' or pergunta == 'SIM':
        sistema_operacional_if()
        pass
    elif pergunta == '2' or pergunta == 'NÃO' or pergunta == 'NAO':
        sistema_operacional_if()
        break
