'''# Задача 1. De la tastatură se introduce un număr întreg N. Să se elaboreze un program care calculează valoarea următoarei expresiei: 𝑓: 𝑁 → 𝑁, 𝑓(𝑛)={𝑛, 𝑛<10; (𝑛 𝑚𝑜𝑑 10)+𝑓(𝑛 𝑑𝑖𝑣 10), 𝑛≥10.
def recursia(n:int):
    if n<10: return n
    else: return (n%10)+recursia(n//10)
    
n=int(input('Введите целое число N: '))
print('Результат:', recursia(n))'''



'''# Задача 2. De la tastatură se introduce un număr întreg N. Să se elaboreze un program care calculează valoarea următoarei expresiei: 𝑓: 𝑁 → 𝑁, 𝑓(𝑛)={2, 𝑛<10; 𝑛+𝑓(𝑛 𝑑𝑖𝑣 10), 𝑛≥10.
def recursia(n:int):
    if n<10: return 2
    else: return n+recursia(n//10)
    
n=int(input('Введите целое число N: '))
print('Результат:', recursia(n))'''



'''# Задача 3. De la tastatură se introduce un număr natural N. Să se elaboreze un program care calculează valoarea sumei: S(n)=1+3+5+...+(2n-1), 𝑛∈𝑁.
def recursia(n:int):
    if n==1: return 1
    else: return (2*n-1)+recursia(n-1)
    
n=int(input('Введите натуральное число N: '))
if n>0: print('Результат:', recursia(n))
else: print('Перепроверьте введённое число')'''



'''# Задача 4. De la tastatură se introduce un număr natural N. Să se elaboreze un program care determină cifra cea mai mare a unui număr natural N.
def recursia(n:int):
    if n<10: return n
    else:
        if n%10>recursia(n//10): return n%10
        else: return recursia(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: print('Результат:', recursia(n))
else: print('Перепроверьте введённое число')'''



'''# Задача 5. De la tastatură se introduc două numere naturale N și X. Să se elaboreze un program care determină numărul de apariții a cifrei X în numărul natural N.
def recursia(n, x:int):
    if n==0: return n
    else: 
        if n%10==x: return 1+recursia(n//10, x)
        else: return recursia(n//10, x)

n=int(input('Введите натуральное число N: '))
x=int(input('Введите X (цифра должна содержаться в числе N): '))
if (n>0) and ((x>=0) and (x<=9)):
    print('Цифра X встречается в числе N', recursia(n, x), 'раз')
else: print('Перепроверьте введённое число')'''



'''# Задача 6. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează descompunerea unui număr natural N în factori primi. Exemplu: 19344=2*2*2*2*2*3*13*31.
def recursia(n:int, x:int=2):
    if n==1: return 0
    if n%x==0:
        print('*'+str(x), end='')
        recursia(n//x, x)
    else: recursia(n, x+1)


n=int(input('Введите натуральное число N: '))
if n>1:
    print(n, end='=')
    x=2
    while n%x!=0:
        x=x+1
    print(x, end='')
    recursia(n//x, x)
else: print('Перепроверьте введённое число')'''
        
        

'''# Задача 7. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează divizorii unui număr natural N.
def recursia(n:int, x:int=1):
    if x>n: return 0
    if n%x==0: print(x, end=' ')
    recursia(n, x+1)

n=int(input('Введите натуральное число N: '))
if n>0:
    print('Делители числа N:', end=' ')
    recursia(n)
else: print('Перепроверьте введённое число')'''      
        
        

'''# Задача 8. De la tastatură se introduce un număr natural N. Să se elaboreze un program care determină numărul de cifre al unui număr natural.
def recursia(n:int):
    if n<10: return 1
    else: return 1+recursia(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: print('Всего цифр:', recursia(n))
else: print('Перепроверьте введённое число')'''
 
 
 
'''# Задача 9. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează inversul unui număr natural N.
def recursia(n:int):
    if n>0: 
        print(n%10, end='')
        recursia(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: 
    print('Обратное число: ', end='')
    recursia(n)
else: print('Перепроверьте введённое число')'''



'''# Задача 10. De la tastatură se introduce un număr natural N. Să se elaboreze un program care calculează 2 la puterea N.
def recursia(n:int):
    if n==0: return 1
    else: return 2*recursia(n-1)
    
n=int(input('Введите натуральное число N: '))
if n>=0: print('Результат:', recursia(n))
else: print('Перепроверьте введённое число')'''



'''# Задача 11. De la tastatură se introduce un număr natural N. Să se elaboreze un program care afișează triunghiul de numere de mai jos:
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
else: print('Перепроверьте введённое число')'''
    
    
    
'''# Задача 12. De la tastatură se introduce un număr natural N. Să se elaboreze un program care determină, dacă un număr natural N are sau nu toate cifrele distincte.
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
else: print('Перепроверьте введённое число')'''



'''# Задача 13. Se citește un vector A cu N elemente numere naturale. Să se elaboreze un program care determină suma elementelor pare dintr-un vector.
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
else: print('Перепроверьте введённое число')'''
        


'''# Задача 14. De la tastatură se introduce un număr natural N. Să se elaboreze un program care elimină cifrele impare dintr-un număr și afișează numărul obținut.
def recursia(n:int):
    if n==0: return 0
    recursia(n//10)
    cifra=n%10
    if cifra%2==0: print(cifra, end='')

n=int(input('Введите натуральное число N: ')) 
if n>0: 
    print('Полученное число:', end='')
    recursia(n)
else: print('Перепроверьте введённое число')'''



'''# Задача 15. De la tastatură se introduc un șir de caractere S și un caracter C. Să se elaboreze un program care determină de câte ori apare caracterul C în șirul de caractere S.
def recursia(s, c:str, i:int):
    if i>=len(s): return 0
    else:
        if s[i]==c: return 1+recursia(s, c, i+1)
        else: return recursia(s, c, i+1)

s=input('Введите строку S: ')
c=input('Введите символ C: ')
if len(c)==1: print('Символ "', c, '" встречается в строке', recursia(s, c, 0), 'раз')
else: print('Нужно ввести только 1 символ')'''



'''# Задача 16. Se citește un vector A cu n elemente numere întregi. Să se elaboreze un program care citește, afișează și construiește doi vectori B și C astfel: vectorul B va conține elementele pare din vectorul A; vectorul C va conține elementele impare din vectorul A.
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
else: print('Перепроверьте введённое число')'''