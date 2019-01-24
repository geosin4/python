# 1. Дано предложение. Заменить группы пробелов одиночными, крайние пробелы удалить.
# Все слова перевести в нижний регистр, первые буквы сделать заглавными.
#
#
# 2. Дана строка. Заменить все ссылки и email на ***** (количество звездочек равно длине заменяемого фрагмента).
# Примеры ссылок: www.site.com, http://site.com и т.п.
#
#
# 3. Пользователь бесконечно вводит e-mail адреса. Вывести только те, которые не повторяются
#
# 1.

def stringChange(s):
    s = s.lower()
    words = s.split(" ")

    return " ".join(list(map(lambda x:x.capitalize(),filter(None, words))))

# 2.

def hyperlinkChange(s):
    words = s.split(" ")

    return ' '.join(["*"*len(x)  if  x[-4:] == '.com' else x for x in words ])

# 3.

def emailChange(s):
    words = s.split(" ")
    return set(words)




