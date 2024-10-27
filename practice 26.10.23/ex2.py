N=int(input("Введите конечное число цикла: "))
i=0
list=[]
while i<N:
    for i in range(-1,N):
        i+=1
        list.append(i)
print(*list)