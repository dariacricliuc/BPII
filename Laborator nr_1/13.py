# Задача 13. Se citește un vector A cu N elemente numere naturale. Să se elaboreze un program care determină suma elementelor pare dintr-un vector.
def recursia(A:int, i:int):
    if i>=len(A): return 0
    else: 
        if A[i]%2==0: return A[i]+recursia(A, i+1)
        else: return recursia(A, i+1)

n=int(input('Введите натуральное число N: ')) 
if n>0:
    A=[0]*n
    i=0
    while i<n:
        A[i]=int(input('Введите элементы массива: '))
        i=i+1

    print('Сумма чётных элементов массива:', recursia(A, 0))
else: print('Перепроверьте введённое число')