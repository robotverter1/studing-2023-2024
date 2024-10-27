rainfall = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

days_without_rain = 0
current_day = 0

while current_day < len(rainfall) and rainfall[current_day] == 0:
    days_without_rain += 1
    current_day += 1

print("Количество первых дней без осадков в мае:", days_without_rain)
