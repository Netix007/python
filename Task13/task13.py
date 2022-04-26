# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def str_com(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    counter = 0
    for i in range(str1_len-str2_len+1):
        temp = str1[i: i+str2_len]
        if temp == str2:
            counter += 1
    return counter

def inp(num):
    str = input(f'Введите {num}-ую строку: ')
    while len(str) == 0:
        str = input('Введите строку: ')
    return str

str1 = inp(1)
str2 = inp(2)
counter1 = str_com(str1, str2)
counter2 = str_com(str2, str1)
print('Количество вхождений строки 2 в строку 1:', counter1)
print('Количество вхождений строки 1 в строку 2:', counter2)
