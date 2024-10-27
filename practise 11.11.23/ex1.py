def pali():
    a=str(input("Введите число, которое хотите проверить: "))
    if a==a[::-1]:
        print("YES")
    else:
        print("NO")
pali()