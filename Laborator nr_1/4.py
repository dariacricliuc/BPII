# Задача 4. De la tastatură se introduce un număr natural N. Să se elaboreze un program care determină cifra cea mai mare a unui număr natural N.
def recursia(n:int):
    if n<10: return n
    else:
        if n%10>recursia(n//10): return n%10
        else: return recursia(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: print('Результат:', recursia(n))
else: print('Перепроверьте введённое число')