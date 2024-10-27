sum_weight=0
count=0
for i in range(5):
    weight = int(input("Введите вес пассажира: "))
    sum_weight+=weight

    if weight>60:
        count+=1
    if sum_weight>300:
        print("Лодка утонула")
        break
if sum_weight<=300:
    print("Лодка утонула!")
print("Количество пассажиров с весом больше 60 кг:", count)