'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

from time import sleep

while True:
    nome = str(input('Digite o seu nome: '))
    if len(nome) <= 3:
        print('O nome que você digitou é muito pequeno. Digite novamente.')
        continue
    else:
        print('Nome aceito.\n')
        break

while True:
    idade = int(input('Digite a sua idade: '))
    if idade < 0 or idade > 150 :
        print('Sua idade deve ser um valor INTEIRO entre 0 e 150.')
        continue
    else:
        print("Sua idade foi registrada.\n")
        break

while True:
    salario = float(input('Digite o seu salário: R$'))
    if salario < 0:
        print('O valor digitado deve ser maior que zero.')
        continue
    else:
        print('O seu salário foi registado.\n')
        break

while True:
    sexo = input('Informe seu sexo [M/F] ').strip().upper()[0]
    if sexo not in 'FfMm':
        print('Dados inválidos.')
        continue
    else:
        print('Sexo {} registrado com sucesso.\n'.format(sexo.upper()))
        break

while True:
    estado = input('Informe seu estado civil [S, C, V D] ').strip().upper()[0]
    if estado not in 'SsCcVvDd':
        print('Dados inválidos.')
        continue
    else:
        print('Estado civil {} registrado.\n'.format(estado.upper()))
        break

sleep(0.1)
print('Fim\n')
sleep(0.3)
print('As informações registradas foram:\n')

print('Nome: {}\n'.format(nome))
print('Idade: {}\n'.format(idade))
print('Salário: R${:.0f}\n'.format(salario))
print('Sexo: {}\n'.format(sexo))
print('Estado civil: {}\n'.format(estado))