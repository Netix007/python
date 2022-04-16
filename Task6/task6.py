# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным
is_error = True
while is_error:
    is_error1 = False
    day = input('Введите число, обозначающее день недели: ')
    try:
        day = int(day)
    except ValueError:
        is_error1 = True
    if (not is_error1):
        day = int(day)
        if (1 <= day <= 7):
            is_error = False 
list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
if (day == 6 or day == 7):
    print(f'{list[day-1]} - выходной день')
else:
    print(f'{list[day-1]} - рабочий день')