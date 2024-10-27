a=int(input("Введите делитель: "))
b=int(input("Введите делимое: "))
try:
    k = b/a 
    print(k)
except ZeroDivisionError:
    print("Error")
