# Задача 12. De la tastatură se introduce un număr natural N. Să se elaboreze un program care determină, dacă un număr natural N are sau nu toate cifrele distincte.
def recursia(n:int, cifra:int):
    if n==0: return False
    if n%10==cifra: return True
    
    return recursia(n//10, cifra)

def diferit(n:int):
    if n<10: return True
    if recursia(n//10, n%10): return False
    
    return diferit(n//10)

n=int(input('Введите натуральное число N: '))
if n>0:
    if diferit(n):
        print('Все цифры числа N различные')
    else:
        print('Все цифры числа N не различные')
else: print('Перепроверьте введённое число')