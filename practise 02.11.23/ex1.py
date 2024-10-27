list=[5, 10, 15, 20, 25, 50, 20]
for i in range(len(list)):
    if list[i]==50:
        list.remove(list[i])
        list.insert(5, 200)
        print(list)
    if list[i]==10:
        list.remove(list[i])
        list.insert(0,10)
        print(list)