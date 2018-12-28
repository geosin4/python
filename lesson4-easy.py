#EASY
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

from random import randint

list1 = [randint(0,i) for i in range(1,20)]

print([i**2 for i in list1])


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit1 = ['bananas','apple','watermellon','mellon','lime']
fruit2 = ['strawberries','lime','ananas','coconut','mellon','apple']
print (set(fruit1).intersection(fruit2))


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

from random import randint
list1 = [randint(0,i) for i in range(1,20)]
list2 = []
for i in list1:
    if i>0 and i%3==0 and i%4!=0:
        list2.append(i)
print(list2)






