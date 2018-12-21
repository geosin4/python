# Easy
#
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.


list = ["watermellon", "melon", "apple", "bananas", "strawberries","cherries"]
for a,b in enumerate(list,1):
    print('{}.{:>13}'.format(a,b))
#
#
# # Задача-2:
# # Даны два произвольные списка.
# # Удалите из первого списка элементы, присутствующие во втором списке.
#

list1 = ['s',12,'m',5,7,'r',9,10,'c','w']
list2 = [5,'t','w',2,7,'y',4,'r']
for i in list1:
    for j in list2:
        if i == j:
            list1.remove(i)
list1.extend(list2)
print(list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


list = [2,4,6,34,67,8,45,9,76,4,8,1]
res_list = []
for i in list:
    if i%2==0:
        i/=4
    else:
        i*=2
    res_list.append(i)
print(res_list)


# Normal
#
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]
#
#

import math
list1 = [4,65,7,32,9,12,79,23,-25,25]
list2 = []
for i in list1:
    if i < 0 :
        continue
    square_r = math.sqrt(i)
    if square_r.is_integer():
        list2.append(int(square_r))
print(list2)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = '03.01.2019'
months = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
days = ["первое","второе","третье","четвертое","пятое","шестое","седьмое","восьмое","девятое","десятое","одиннадцатое","двенадцатое","тринадцатое","четырнадцатое","пятнадцатое","шестнадцатое","семнадцатое","восемнадцатое","девятнадцатое","двадцатое","двадцать первое","двадцать второе","двадцать третье","двадцать четвертое","двадцать пятое","двадцать шестое","двадцать седьмое","двадцать восьмое","двадцать девятое","тридцатое","тридцать первое"]
text_date = []
for day in days:
    if int(date[:2]) == days.index(day) + 1:
        text_date.append(day)
        break

for month in months:
    if int(date[3:5]) == months.index(month)+1:
        text_date.append(month)
        break

text_date.append(date[6:])
text_date.append('года')
print(*text_date)


#
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
#


import random
n = int(input('Input n: '))
list = []
for i in range(n):
    list.append(random.randint(-100,100))
print(*list)


# Hard
#
# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?
#

import string
text = input('Input your text: ')

text = text.lower()

for punct in string.punctuation:
    while punct in text:
        text = text.replace(punct, "")
print(text)

 #Number of words
num_words = len([i for i in text.split() if i.isalnum()])
print(num_words)


count = 0 #Number of letters
for j in text:
    for  i in string.ascii_lowercase:
        if i == j:
            count+=1
        else:
            continue
print(count)


# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра
#
text1 = input('Input first text: ')
text2 = input('Input second text: ')

common_words = []

text1 = text1.lower()
text2 = text2.lower()

text1_words = [i for i in text1.split() if i.isalnum()]
text2_words = [j for j in text2.split() if j.isalnum()]
#
for i in text1_words:
    for j in text2_words:
        if i == j:
            common_words.append(i)
        else:
            None
print(common_words)


# EXTRA
# Есть два словаря. Один это рецепт блюда, второй это список продуктов, которые есть в ходильнике.
#
# Ключ это название продукта, значение - это количество.
#
# Нужно сравнить два словаря и дать словарь, в котором будет список покупок
# Если для рецепта всё есть, то сказать что ничего не нужно
# Разницей по измерению гр, мл, шт. Пренебречь


receipt = {'rostbeef':1,'salat':1, 'salt':10, 'pepper':10, 'oil':50, 'onion':2}
refrig_list = {'onion':1, 'carrot':3, 'watermellon':1,'butter':1, 'rostbeef':2}
buy_list = []
for i in receipt.keys():
    if i not in refrig_list:
        buy_list.append(i)


for a,b in enumerate(buy_list,1):
     print('{}.{}'.format(a,b))


