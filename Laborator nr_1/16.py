# Задача 16. Se citește un vector A cu n elemente numere întregi. Să se elaboreze un program care citește, afișează și construiește doi vectori B și C astfel: vectorul B va conține elementele pare din vectorul A; vectorul C va conține elementele impare din vectorul A.
def recursia(A:int, i:int, B:int, C:int):
    if i>=len(A): return B, C
    if A[i]%2==0: B.append(A[i])
    else: C.append(A[i])     
    return recursia(A, i+1, B, C)

def afisare(V):
    i=0
    while i<len(V):
        print(V[i], end=" ")
        i=i+1
    print()

n=int(input('Введите натуральное число N: ')) 
if n>0:
    A=[0]*n
    i=0
    while i<n:
        A[i]=int(input('Введите элементы массива A: '))
        i=i+1

    B, C=recursia(A, 0, [], [])
    print('Массив B с чётными элементами:')
    afisare(B)
    print('Массив C с нечётными элементами:')
    afisare(C)
else: print('Перепроверьте введённое число')