a=str(input("Введите различные символы: "))
b=str(input("Введите символ, который хотите проверить на повторение: "))
if a.count(b)>1:
    print("Yes")
else:
    print("No")