par = 0
impar = 0

for n in range(10):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1

    else:
        impar += 1

print('Foram digitados {} número(s) pare(s) e {} número(s) ímpar(es).'.format(par, impar))