N=int(input("введите число: "))
sum=0
if N<0:
        print("Так низя")
else:
    for i in range(N*2,(N+1)*2):
        sum+=i*2
print(sum)