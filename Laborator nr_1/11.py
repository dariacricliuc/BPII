# Задача 11. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează triunghiul de numere de mai jos:
#   1 
#   1 2
#   ..........
#   1 2 3 ... n-1
#   1 2 3 ... n-1 n
def linia(i:int, n:int):
    if i<=n:
        print(i, end=' ')
        linia(i+1, n)

def triunghi(k:int, n:int):
    if k<=n:
        linia(1, k)
        print()
        triunghi(k+1, n)

n=int(input('Введите натуральное число N: '))
if n>0: triunghi(1, n)
else: print('Перепроверьте введённое число')