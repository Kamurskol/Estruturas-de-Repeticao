#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

a = 0
b = 1

while (a < 500):
    print(a)
    c = a + b
    a = b
    b = c
