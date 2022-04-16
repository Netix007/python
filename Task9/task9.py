# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
def func():
    is_error = True
    while is_error:
        is_error1 = False
        number = input('Введите номер четверти: ')
        try:
            number = int(number)
        except ValueError:
            is_error1 = True
            print('некорректные данные, номер четверти - целое число от 1 до 4')
        if (not is_error1):
            number = int(number)
            if (1 <= number <= 4):
                is_error = False
            else:
                print('некорректные данные, номер четверти - целое число от 1 до 4')
    return number
a = func()
if a == 1:
    print('Допустимые значения координат для точек из I четверти: X > 0, Y > 0')
elif a == 2:
    print('Допустимые значения координат для точек из II четверти: X < 0, Y > 0')
elif a == 3:
    print('Допустимые значения координат для точек из III четверти: X < 0, Y < 0')
elif a == 4:
    print('Допустимые значения координат для точек из IV четверти: X > 0, Y < 0')