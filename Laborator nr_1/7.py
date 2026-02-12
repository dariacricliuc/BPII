# Задача 7. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează divizorii unui număr natural N.
def recursia(n:int, x:int=1):
    if x>n: return 0
    if n%x==0: print(x, end=' ')
    recursia(n, x+1)

n=int(input('Введите натуральное число N: '))
if n>0:
    print('Делители числа N:', end=' ')
    recursia(n)
else: print('Перепроверьте введённое число')