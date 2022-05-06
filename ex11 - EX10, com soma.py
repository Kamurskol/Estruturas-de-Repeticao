n1 = int(input())
n2 = int(input())
print('\n')
soma = 0

for inteiro in range(n1, n2):

    print(inteiro)
    soma += inteiro

print('\nA soma dos números é {}.'.format(soma))