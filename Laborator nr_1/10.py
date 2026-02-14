# Задача 10. De la tastatură se introduce un număr natural N. Să se elaboreze un program care calculează 2 la puterea N.
def recursia(n:int):
    if n==0: return 1
    else: return 2*recursia(n-1)
    
n=int(input('Введите натуральное число N: '))
if n>=0: print('Результат:', recursia(n))
else: print('Перепроверьте введённое число')