a=list(map(int,input("Введите баллы за 3 дисциплины: ").split()))
b=0
def marks():
    global a
    global b
    for i in range(len(a)):
        if len(a)==3:
            b=(a[0]+a[1]+a[2])/3
            if b>=90 and b<=100:
                print(f"Ваша оценка: A")
                break
            elif 80<=b<90 :
                print(f"Ваша оценка: B")
                break
            elif 70<=b<80:
                print(f"Ваша оценка: C")
                break
            elif 60<=b<70:
                print(f"Ваша оценка: D")
                break
            elif 0<=b<60:
                print(f"Ваша оценка: F")
                break
marks()
if len(a)>3 or len(a)<3:
    print(f"Необходимо ввести оценки за 3 дисциплины, попробуйте снова.")
