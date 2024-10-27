import random

symbols="BCDFGHJKLMNPQRSTVWXYZAEIOUbcdfghjklmnpqrstvwxyzaeiou!#$%&"
d=int(input("Введите количество символов в желаемом пароле: "))
b=''
for i in range(d):
    b+=random.choice(symbols)
print(b)