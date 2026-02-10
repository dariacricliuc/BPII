# Задача 2. De la tastatură se introduce un număr întreg N. Să se elaboreze un program care calculează valoarea următoarei expresiei: 𝑓: 𝑁 → 𝑁, 𝑓(𝑛)={2, 𝑛<10; 𝑛+𝑓(𝑛 𝑑𝑖𝑣 10), 𝑛≥10.
def recursia(n:int):
    if n<10: return 2
    else: return n+recursia(n//10)
    
n=int(input('Введите целое число N: '))
print('Результат:', recursia(n))