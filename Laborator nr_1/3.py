# Задача 3. De la tastatură se introduce un număr natural N. Să se elaboreze un program care calculează valoarea sumei: S(n)=1+3+5+...+(2n-1), 𝑛∈𝑁.
def recursia(n:int):
    if n==1: return 1
    else: return (2*n-1)+recursia(n-1)
    
n=int(input('Введите натуральное число N: '))
if n>0: print('Результат:', recursia(n))
else: print('Перепроверьте введённое число')