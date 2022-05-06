popA = 80000
popB = 200000

crescA = 1.03
crescB = 1.015

ano = 1
while (popA <= popB):
    popA *= crescA
    popB *= crescB
    ano += 1
    print('{:.0f}'.format(popA))
    print('{:.0f}\n'.format(popB))

print('Serão necessários {} anos para a população do país A ser amior que a população do país B.'.format(ano))