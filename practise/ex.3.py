a=int(input("Введите 1 число:"))
b=int(input("Введите 2 число:"))
if b<a:
    a+=1
    for i in range(b,a,1):
        print(i,end=" ")
else:
    a-=1
    for i in range(b,a,-1):
        print(i,end=" ")
