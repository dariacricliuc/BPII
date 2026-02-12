# Задача 9. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează inversul unui număr natural N.
def recursia(n:int):
    if n>0: 
        print(n%10, end='')
        recursia(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: 
    print('Обратное число: ', end='')
    recursia(n)
else: print('Перепроверьте введённое число')