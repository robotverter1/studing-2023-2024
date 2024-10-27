import random
a=int(input("Введите начало списка: "))
b=int(input("Введите конец списка: "))
n=int(input("Введите колличество чисел в интервале: "))
list=[]
for i in range(n):   
    random_list=random.randint(a,b)
    list.append(random_list)
print(*list)
input()