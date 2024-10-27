list=[1, 2, 3, 4, 5, 6, 7]
list1=[]
for i in range(len(list)):
    list[i]=list[i]*list[i]
    list1.append(list[i])
    print(list1)
    