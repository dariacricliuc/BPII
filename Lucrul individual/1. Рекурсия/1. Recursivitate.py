'''# 4. Elaborează o procedură recursivă P1 care afişiază imaginea inversă a unui număr natural N. De exemplu, dacă N=1234, atunci se va afişa 4321.
def P1(n:int):
    if n>0: 
        print(n%10, end='')
        P1(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: 
    print('Обратное число: ', end='')
    P1(n)
else: print('Перепроверьте введённое число')'''


   
'''# 6. Elaborează o funcţie recursivă F1 care returnează imaginea inversă a unui număr natural N. De exemplu, dacă N=1234, atunci se va afişa 4321.
def F1(n:int):
    if n==0: return ''
    else: return str(n%10)+F1(n//10)

n=int(input('Введите натуральное число N: '))
if n>0: print('Обратное число: ', F1(n))
else: print('Перепроверьте введённое число')'''