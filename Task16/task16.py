# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму.
# Например n = 4: результат [2, 2.25, 2.37037037037, 2.44140625] сумма элементов - 9.06177662037037

is_Error = True
while is_Error:
    n = input('Введите число n = ')
    try:
        int(n)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(n) > 0:
       n = int(n)
    else:
        is_Error = True
sum = 0
list = []
for i in range(n):
    num = (1+1/(i+1))**(i+1)
    list.append(num)
    sum += num
print(list)
print('Сумма элементов:', sum)