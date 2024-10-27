list=input("Введите список значений через пробел: ").split()
for i in range(1, len(list)-2,1):
    if len(list)%2==0:
        list[i],list[i+2]=list[i+2],list[i]
        print(list)
        break
    elif len(list)%2!=0:
        list[i],list[i+2]=list[i+2],list[i]
        list[-1]=list[0]
        print(list)
        break
        
        
        
