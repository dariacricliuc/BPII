# Задача 5. De la tastatură se introduc două numere naturale N și X. Să se elaboreze un program care determină numărul de apariții a cifrei X în numărul natural N.
def recursia(n, x:int):
    if n==0: return n
    else: 
        if n%10==x: return 1+recursia(n//10, x)
        else: return recursia(n//10, x)

n=int(input('Введите натуральное число N: '))
x=int(input('Введите X (цифра должна содержаться в числе N): '))
if (n>0) and ((x>=0) and (x<=9)):
    print('Цифра X встречается в числе N', recursia(n, x), 'раз')
else: print('Перепроверьте введённое число')