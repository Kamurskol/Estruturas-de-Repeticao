#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.


N = int(input())
a = 0
b = 1

for i in range(N):
    if i == N-1:
        print(a)
    else:
        print(a)
    c = a + b
    a = b
    b = c
