# Задача 14. De la tastatură se introduce un număr natural N. Să se elaboreze un program care elimină cifrele impare dintr-un număr și afișează numărul obținut.
def recursia(n:int):
    if n==0: return 0
    recursia(n//10)
    cifra=n%10
    if cifra%2==0: print(cifra, end='')

n=int(input('Введите натуральное число N: ')) 
if n>0: 
    print('Полученное число:', end='')
    recursia(n)
else: print('Перепроверьте введённое число')