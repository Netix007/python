# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

from re import I, S


is_Error = True
while is_Error:
    n = input('Введите количество членов последовательности n = ')
    try:
        int(n)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(n) > 0:
       n = int(n)
    else:
        is_Error = True
s = [1]
for i in range(1,n):
     s.append(-3*s[i-1])
print(s)