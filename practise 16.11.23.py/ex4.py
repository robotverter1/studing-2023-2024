a=list(map(int,input("Введите числа в массив: ").split()))
sum=0
for i in range(len(a)):
    if a[i]>0:
        sum=sum+a[i]
    if sum==0:
        print("Сумма не получилась")
print(sum)