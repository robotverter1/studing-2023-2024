a=list(map(int,input("Введите числа в массив: ").split()))
b=0
lst1=[]
for i in range(len(a)):
    if a[i]<0:
        lst1.append(a[i])
    if a[i]>0:
        b+=1
print(b,sum(lst1))