# Подсчитать сумму цифр в вещественном числе.

def inp_float():
    is_Error = True
    while is_Error:
        n = input('Введите вещественное число n = ')
        try:
            float(n)
            is_Error = False
        except ValueError:
            is_Error = True
    return n
#n = 1.10258
str = inp_float()
sum = 0
for i in range(len(str)):
    if str[i] != '.' and str[i] != '-':
        sum += int(str[i])
print('Сумма цифр в числе:', sum)