# 2. Найти максимальное из пяти чисел
digits = [1, 18, -27, 23, 0]
max_digit = digits[0]
for i in digits:
    if i > max_digit:
        max_digit = i
print(max_digit)