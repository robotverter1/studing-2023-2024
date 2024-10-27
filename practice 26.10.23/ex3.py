N=int(input("Введите конечное число цикла: "))
list=[]
while N>0:
    for i in range(N+1,0,-1):
        i-=1
        list.append(i)
    break
print(*list)
