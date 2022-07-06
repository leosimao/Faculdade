#Apresente na tela os números de 1 a 100.

# cont = 1
# while(cont <= 100):
#     print(cont)
#     cont += 1

#Faça a soma dos números de 1 a 100 e apresente somente o resultado.

# soma = 0
# cont = 0
# while(cont < 100):
#     soma += cont
#     cont += 1
# print(soma)


#Apresente na tela somente os números pares entre 50 e 100

# cont = 50
# while(cont <= 100):
#     if(cont % 2 == 0):
#         print(cont)
#     cont += 1

#Apresente na tela somente os números ímpares entre 1 e 50.

# cont = 1
# while(cont <= 50):
#     if(cont % 2 == 1):
#         print(cont)
#     cont += 1

#Apresente na tela somente a soma dos números pares entre 1 e 100.

# cont = 1
# soma = 0
# while(cont <= 100):
#     if(cont % 2 == 0):
#         soma += cont
#         print(soma)
#     cont += 1
# print(soma)
        
#Apresente na tela os números de X a Y (peça para o usuário informar os valores de X e de Y).

# x = int(input("Digite o primeiro valor: "))
# y = int(input("Digite o segundo valor: "))

# while(x <= y):
#     print(x)
#     x += 1

#Faça a soma dos números de X a Y e apresente somente o resultado (peça para o usuário informar os valores de X e de Y).

# x = int(input("Digite o primeiro valor: "))
# y = int(input("Digite o segundo valor: "))

# soma = 0
# while(x <= y):
#     soma += x
#     x += 1
# print(soma)

#Apresente na tela somente os números ímpares entre X e Y (peça para o usuário informar os valores de X e de Y).

# x = int(input("Digite o primeiro valor: "))
# y = int(input("Digite o segundo valor: "))

# while(x <= y):
#     if(x % 2 == 1):
#         print(x)
#     x += 1

#Faça um programa para calcular a tabuada:
    #do 1 ao 10 para um número informado pelo usuário.

# cont = 1
# user = int(input("Digite qual é a tabuada desejada: "))
# while(cont <= 10):
#     result = user * cont
#     print(f"{user} x {cont} = {result}")
#     cont += 1

    #do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y).

# user_tab = int(input("Digite a tabuada desejada: "))
# user_x = int(input("Digite onde a tabuada deve começar: "))
# user_y = int(input("Digite onde a tabuada deve finalizar "))

# if(user_y < user_x):
#     tr = user_y
#     user_y = user_x
#     user_x = tr

# if(user_tab != 0):
#     while(user_x <= user_y):
#         result = user_x * user_tab
#         print(f"{user_tab} x {user_x} = {result}")
#         user_x += 1
# else:
#     print("Impossivel calcular valores multiplicados por 0!")

#Faça um programa que peça um número para o usuário e apresente na tela seu fatorial.

# user = int(input("Digite o número que queira fatoriar: "))
# cont = user
# while(cont > 1):
#     cont -= 1
#     user *= cont
#     print(user)

#Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que peça ao usuário qual o termo final (N) e calcule o valor de H. 

# user = int(input("Digite um valor para continuarmos o calculo... "))
# h = 1 
# result = 0
# while(h < user):
#     result += (1/h)
#     h += 1
#     print(f"O Valor de h é {result:.2f}")

#Faça um programa em Python “Acertou, ganhou!” o programa deverá:
    #Gerar um número aleatório entre 1 e 10 e pedir para o usuário digitar números até que acerte. Ao acertar, apresente uma mensagem parabenizando e finalize o programa.

# import random as rd

# num = rd.randint(1, 10)
# user = int(input("Será que você está com sorte? "))
# cont = 1

# while(user != num):
#     if(user >= 1 and user <= 10):
#         print(f"O número aleatório foi {num}")
#         print(f"O número digitado foi {user}")
#         user = int(input("Não foi dessa vez tente novamente: "))
#         num = rd.randint(1, 10)
#         cont += 1
#     else:
#         print("Número inválido, digite um valor entre 1 e 10")
#         exit()

# print("Parabéns você acertou o número da sorte!")
# print(f"Você tentou {cont} vezes!")

# Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).
# import time as tm
# import math as mt

# choose = 0
# while(choose != 4):
#     if( choose != 4):
#         print('''
#             ==== MENU ====
#             1. Par ou impar
#             2. Potência
#             3. Raiz quadrada
#             4. Sair       
#         ''')
#         choose = int(input("Escolha uma opção: "))
#         if(choose == 1):
#             user_vlr = int(input("Digite um valor para sabermos se é par ou impar: "))
#             calc = user_vlr % 2 
#             if(calc == 0):
#                 print(f"O número {user_vlr} é par!")
#             else:
#                 print(f"O número {user_vlr} é impar!")
#             tm.sleep(2)
#         elif(choose == 2):
#             user_vlrx = int(input("Digite o número que deseja que seja elevado!: "))
#             user_vlry = int(input("Digite o expoente desejado "))
#             calc = mt.pow(user_vlrx, user_vlry)
#             print(f"A potência de {user_vlrx} elevado a {user_vlry} é igual a {calc}")
#             tm.sleep(2)
#         elif(choose == 3):
#             user_vlr = float(input("Digite o valor que deseja realizar a raiz dele "))
#             calc = mt.sqrt(user_vlr)
#             print(f"A raiz quadrada de {user_vlr} é igual a {calc:.02f}!")
#             tm.sleep(2)
#     else:
#         print("Saindo do programa...")
#         tm.sleep(3)
#         exit()

# import time as tm
# import math as mt


# def menu():
#     print('''
#         ===== MENU =====
#         1. PAR OU IMPAR
#         2. POTÊNCIA
#         3. RAIZ QUADRADA
#         4. SAIR
#     ''')
#     user = int(input("Escolha uma opção: "))
#     return user

# option = 0

# while(option != 4):
#     option = menu()
#     if(option == 1):
#         user_num = int(input("Digite um valor para saber se é par ou impar: "))
#         if(user_num % 2 == 0):
#             print(f"O número {user_num} é par!")
#         else:
#             print(f"O número {user_num} é impar!")
#         tm.sleep(1)
#     elif(option == 2):
#         user_vlrx = int(input("Digite o valor que deseja elevar: "))
#         user_vlry = int(input("Digite o expoente: "))
#         calc = mt.pow(user_vlrx, user_vlry)
#         print(f"A potência entre {user_vlrx} elevado a {user_vlry} é igual {calc}")
#         tm.sleep(1)
#     elif(option == 3):
#         user_vlr = int(input("Digite um valor para sabermos sua raiz! "))
#         calc = mt.sqrt(user_vlr)
#         tm.sleep(1)
#         print(f"A raiz quadrada de {user_vlr} é igual a {calc:.02f}")
#     elif(option == 4):
#         print("Tudo bem! Nos vemos em breve...")
#         tm.sleep(1)
#         print("Desligando...")
#         tm.sleep(2)
#         exit()
#     else:
#         print("Opção inválida digite novamente! ")
#         tm.sleep(0.5)

# i = 100
# cont = 0
# while(i > 1):
#     if(i % 4 == 0):
#         cont += 1
#     i -= 1

# print(f"Entre 100 e 1 existe {cont} divisiveis por 4")

import time as tm

def menu():
    print('''
        ==== MENU ====
        1. Tabuada do 1 ao 10 de acordo com o valor escolhido
        2. Apresentar os multiplos do valor escolhido entre 1 e 100
        3. Apresentar a soma dos valores de 1 a 100
        4. Sair
        ==============    
    ''')
    user = int(input("Digite uma opção: "))
    return user

opc = 0

while(opc != 4):
    opc = menu()
    if(opc == 1):
        user_vlr = int(input("Digite um valor para multiplicarmos: "))
        cont = 1
        while(cont <= 10):
            calc = user_vlr * cont
            print(f"{user_vlr} x {cont} = {calc}")
            cont += 1
        tm.sleep(1)
    elif(opc == 2):
        user_vlr = int(input("Digite um valor para sabermos seus multiplos: "))
        