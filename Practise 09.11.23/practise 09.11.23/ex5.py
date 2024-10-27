x1 = int(input("Номер столбца для первой клетки: "))
y1 = int(input("Номер строки для первой клетки: "))
x2 = int(input("Номер столбца для второй клетки: "))
y2 = int(input("Номер строки для второй клетки: "))
xod_konem1 = abs(x1 - x2)
xod_konem2 = abs(y1 - y2)
if  xod_konem1== 1 and xod_konem2  == 2 or xod_konem1 == 2 and xod_konem2  == 1:
    print('YES')
else:
    print('NO')