popA = int(input('Digite a população do país A: '))
popB = int(input('Digite a população do país B: '))

crescA = float(input('Informe a taxa de crescimento do país A: '))
crescB = float(input('Informe a taxa de crescimento do país B: '))

ano = 1

while (popA <= popB):
    popA *= crescA
    popB *= crescB
    ano += 1
    print('{:.0f}'.format(popA))
    print('{:.0f}\n'.format(popB))

print('Serão necessários {} anos para a população do país A ser amior que a população do país B.'.format(ano))