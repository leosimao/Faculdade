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
#user_tab = int(input("Digite a tabuada desejada: "))
#user_x = int(input("Digite onde a tabuada deve começar: "))
#user_y = int(input("Digite onde a tabuada deve finalizar "))
#
#if(user_y < user_x):
#    tr = user_y
#    user_y = user_x
#    user_x = tr
#
#if(user_tab != 0):
#    while(user_x <= user_y):
#        result = user_x * user_tab
#        print(f"{user_tab} x {user_x} = {result}")
#        user_x += 1
#else:
#    print("Impossivel calcular valores multiplicados por 0!")
