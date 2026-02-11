# Задача 6. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează descompunerea unui număr natural N în factori primi. Exemplu: 19344=2*2*2*2*2*3*13*31.
def recursia(n:int, x:int=2):
    if n==1: return 0
    if n%x==0:
        print('*'+str(x), end='')
        recursia(n//x, x)
    else: recursia(n, x+1)


n=int(input('Введите натуральное число N: '))
if n>1:
    print(n, end='=')
    x=2
    while n%x!=0:
        x=x+1
    print(x, end='')
    recursia(n//x, x)
else: print('Перепроверьте введённое число')