list=[1, 32,6, 3/2, "abcd",tuple(), {},  dict,  None, ]
a=int(input("Введите число: "))
b=str(input("Введите второе str значение: "))
list.append(a)
list.append(b)
for i in range(len(list)):  
    print(type(len(list[0:i])))
