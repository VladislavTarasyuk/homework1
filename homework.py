year = int(input("Введите год: "))
if year % 400 == 0:
    print(year, "- високосный год")
elif year % 100 == 0:
    print(year, "- не високосный год")
elif year % 4 == 0:
    print(year, "- високосный год")
else:
    print(year, "- не високосный год")

