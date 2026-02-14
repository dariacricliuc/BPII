# Задача 15. De la tastatură se introduc un șir de caractere S și un caracter C. Să se elaboreze un program care determină de câte ori apare caracterul C în șirul de caractere S.
def recursia(s, c:str, i:int):
    if i>=len(s): return 0
    else:
        if s[i]==c: return 1+recursia(s, c, i+1)
        else: return recursia(s, c, i+1)

s=input('Введите строку S: ')
c=input('Введите символ C: ')
if len(c)==1: print('Символ "', c, '" встречается в строке', recursia(s, c, 0), 'раз')
else: print('Нужно ввести только 1 символ')