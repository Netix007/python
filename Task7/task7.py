# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def fun(x, y, z):
    if (not (x or y or z) == ((not x) and (not y) and (not z))):
        result = True
    else:
        result = False
    return result

f1 = fun(False, False, False)
f2 = fun(False, False, True)
f3 = fun(False, True, False)
f4 = fun(False, True, True)
f5 = fun(True, False, False)
f6 = fun(True, False, True)
f7 = fun(True, True, False)
f8 = fun(True, True, True)
if (f1 and f2 and f3 and f4 and f5 and f6 and f7 and f8):
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно')