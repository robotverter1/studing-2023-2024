a=int(input("Введите число:"))
n=1
sum=0
if a<0:
    print("Так низя")
else:
    for i in range(n,a+1):
        sum+=n/i
print(sum)