m=int(input("Введите количество лекций: "))
a=str(input("Сидоров С.С \nИванов И.И \nПупкин П.П \nКостин К.К"))
list1=[]
while list1!=a:
    for i in range(len(list1)):
        list1.append(a[i])
        print(list1)
        print("Общее количество студентов", len(list1))
    print()
    break
f=str(input("Введите студентов: ").split())
list=[]
r=0
while list!=f:
    for j in range(len(f)):
        r+=1
        list.append(f[j])
    sorted(list)
    break
print("Фамилии присутствовавших студентов: ", f," Количество студентов: ", r/10)