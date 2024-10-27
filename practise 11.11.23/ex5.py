a=list(map(int,input("Введите 6 числел: ").split()))
b=0
for i in range(len(a)):
    if a[i]>0:
        b+=1
print(b)