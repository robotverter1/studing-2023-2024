N=int(input("Введите количество чисел: "))
srar=[]
for i in range(N):
    num=float(input("Введите числа: "))
    srar.append(num)

negativ_sum=0
positiv_nums=1
for num in srar:
    if num<0:
        negativ_sum+=num
    elif num >0:
        positiv_nums*=num
negative_count=sum(num<0 for num in srar)
positive_count=sum(num>0 for num in srar)

negativ= negativ_sum/negative_count
if negative_count !=0:
    print("Среднее арифметическое отрицательных чисел: ", negativ)
    print("Произведение положительных чисел: ", positive_count)