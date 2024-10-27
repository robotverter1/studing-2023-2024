def vklad():   
    P=int(input("Введите проценты по вкладу:"))
    X=int(input("Введите сумму вклада в рублях: "))
    Y=int(input("Введите вложенные копейки: "))
    start_capital=X*100 +Y
    end_capital=int(start_capital*(P+100)/100)
    print(f"{end_capital//100}.{end_capital%100}")
vklad()