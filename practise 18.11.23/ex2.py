def set_alarm():
    x=str(input(f"Есть ли у вас работа? Если да то введите yes, если нет то no: "))
    y=str(input(f"В отпуске ли вы? Если да то введите yes, если нет то no: "))
    if x=='yes' and y=='yes':
        print(f"Вы можете не заводить будильник, ведь вы дома.")
    elif x=='yes' and y=='no':
        print(f"Заведите будильник, вам завтра на работу.")
    elif x=='no' and y=='yes':
        print(f"Вам не нужно заводить будильник, вы свободный человек.")
    elif x=='no' and y=='no':
        print(f"Вам не нужен будильник, вы свободны.")
    else:
        print("Что-то идёт не так")
set_alarm()