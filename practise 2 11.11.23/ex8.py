a=float(input("Введите расстояние, которое предстоит проехать: "))
b=float(input("Введите расход топлива: "))
if a>=0 or b>=0:
    print(f"Необходимое количество топлива для поездки {round(a/b)}л.")