# Задача 8. De la tastatură se introduce un număr natural N. Să se elaboreze un program care determină numărul de cifre al unui număr natural.
def recursia(n:int):
    if n<10: return 1
    else: return 1+recursia(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: print('Всего цифр:', recursia(n))
else: print('Перепроверьте введённое число')