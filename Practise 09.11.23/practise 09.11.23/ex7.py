N=int(input("Введите длинну бассейна: "))
M=int(input("Введите ширину бассейна: "))
x=int(input("Введите расстояние от мальчика до длинного бортика: "))
y=int(input("Введите расстояние от мальчика до короткого бортика: "))
if N-x>x or M-y>y:
    if M < N and N > x and N > y and M > x and M > y:
        if x < y:
            print(f"Быстрее доплыть до длинного бортика: {x}")
        elif x == y:
            print("В обе стороны расстояние одинаково")
        else:
            print(f"Быстрее доплыть до короткого бортика: {y}")
    elif M == y or N == x:
        print("Бортик рядом")
    else:
        print("Бортик найти не удалось")
elif N-x>x:
    print(N-x)
elif M-y>y:
    print(N-y)