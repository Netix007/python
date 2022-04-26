# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

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
fact = 1
list = []
for i in range(1, n+1):
    fact *= i
    list.append(fact)
print(list)