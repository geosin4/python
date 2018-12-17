#max sign in number
import random
x = random.randint(1,10000)
list = []
for i in str(x):
    list.append(int(i))
print(max(list))