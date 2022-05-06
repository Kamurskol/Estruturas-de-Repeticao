#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome= input('Digite seu nome de usuário: ')
    senha = input('Digite a sua senha.')

    if senha != nome:
        print('Informações salvas.')
        break
    else:
        print('Seu nome e senha não podem ser iguais!')
        continue
