from datetime import date
today= date.today()
products = {
    "Молоко": date(2023,11,13),
    "Хлебушек": date(1933, 2, 11),
    "Яблоко": date(2023, 11, 13)
}
for product, ex in products.items():
    if today <= ex:
        print(f"Данный продукт {product} годен")
    else:
        print(f"Данный продукт {product} не годен")