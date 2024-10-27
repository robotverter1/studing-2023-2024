N=int(input("Введите число: "))
list=[]
list.extend(range(1,N))
for i in range(len(list)):
    list[i]=list[i]*list[i]
    
print(list)