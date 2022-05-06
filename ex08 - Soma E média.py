soma = 0
for i in range(5):
    nota = float(input('Digite um número: '))
    soma += nota

print('A soma dos números é {}.\n'.format(soma))
print('A média é {:.2f}.'.format(soma/5))
