# Реализовать алгоритм перемешивания списка.

from random import randint

list = [1,2,3,4,5]
for i in range(len(list)):
    j = randint(0, i)
    list[i], list[j] = list[j], list[i]
print(list)
