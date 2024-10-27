str="this day is: the most :important in my live"
if str.count(":")==0:
    print("Двоеточия нет")
elif str.count(":")==1:
    begin=str.split(":")[0]
    last=str.split(":")[-1]
    print(begin+" "+ last)
else:
    begin=str.split(":")[0]
    last=str.split(":")[-1]
    print(begin+" "+ last)