print("Решите пример: 4*10 - 54")
a=int(input())
if a!=346:
    print("Ответ неверен.", "Правильный ответ:", 346)
if a==346:
    print("Вы правильно ответили!")



a1=float(input("Введите первое значение:"))
a2=float(input("Введите первое значение:"))
a3=float(input("Введите третье значение:"))
a4=float(input("Введите четвёртое значение:"))
i=0
a1+=a2
a3+=a4
i=round(a1/a3,2)
print(i)