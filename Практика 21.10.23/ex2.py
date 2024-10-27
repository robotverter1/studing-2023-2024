print("Введите 5 чисел: ")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
list=[a,b,c,d,e]
for i in range(len(list)):
    if list.index(list[i])==list.index(list[i]):
        i+=1
        print("Элемент ", i, "не является уникальным.")
    
