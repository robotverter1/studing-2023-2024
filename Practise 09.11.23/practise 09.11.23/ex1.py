def time_part():
    lesson=int(input("Введите номер урока: "))
    time=lesson*45 + (lesson//2)*5 + ((lesson+1)//2-1)*15
    minutes = time%60
    hour = time//60 + 9
    if minutes < 10:
        print(f"{hour}:0{minutes}")
    else:
        print(f"{hour}:{minutes}")
time_part()
