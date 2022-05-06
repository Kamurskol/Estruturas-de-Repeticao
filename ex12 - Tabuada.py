n = int(input('Digite um número para ver sua tabuada: '))
print('Tabuada de {}:\n'.format(n))
for c in range(1, 11):

    print('{} x {} = {}'.format(n, c, c*n))
