# 1
day = int(input("Введіть номер дня тижня (1-7): "))
match day:
    case 1:
        print("Понеділок")
    case 2:
        print("Вівторок")
    case 3:
        print("Середа")
    case 4:
        print("Четвер")
    case 5:
        print("П'ятниця")
    case 6:
        print("Субота")
    case 7:
        print("Неділя")

# 2
mounth = int(input("Введіть номер дня тижня (1-7): "))
match mounth:
    case 1:
        print("Січень")
    case 2:
        print("Лютий")
    case 3:
        print("Березень")
    case 4:
        print("Квітень")
    case 5:
        print("Травень")
    case 6:
        print("Червень")
    case 7:
        print("Липень")
    case 8:
        print("Серпень")
    case 9:
        print("Вересень")
    case 10:
        print("Жовтень")
    case 11:
        print("Листопад")
    case 12:
        print("Грудень")

# 3
suma = float(input("Введіть суму покупки:"))
age = int(input("Введіть свій вік:"))
if age < 18:
    print(f"До сплати {suma - (suma * 0.1)}")
elif 18 <= age < 60:
    print(f"До сплати {suma - (suma * 0.05)}")
elif age >= 60:
    print(f"До сплати {suma - (suma * 0.15)}")

# 4
# Введення оцінок
p1 = int(input("Введіть оцінку з першого предмета (1-5): "))
p2 = int(input("Введіть оцінку з другого предмета (1-5): "))
p3 = int(input("Введіть оцінку з третього предмета (1-5): "))

if p1 < 3 or p2 <3 or p3 <3:
    print("Незадовільно")
elif p1 >= 4 and p2 >= 4 and p3 >= 4:
    print("Відмінно")
else:
    print("Задовільно")


# 5
p1 = int(input("Оцінка 1: "))
p2 = int(input("Оцінка 2: "))
p3 = int(input("Оцінка 3: "))
p4 = int(input("Оцінка 4: "))
if  p1 < 3 or p2 < 3 or p3 < 3 or p4 < 3:
    print("Вас не допущено до іспиту")
elif p1 >= 4 and p2 >= 4 and p3 >= 4 and p4 >= 4:
    print("Вас допущено до іспиту з відзнакою")
else:
    print("Вас допущено до іспиту")

# 6
age = int(input("Введіть вік автомобіля: "))
probig = int(input("Введіть пробіг автомобіля: "))

if age < 3 and probig <= 30000:
    print("Автомобіль у відмінному стані")
elif age <= 10 and probig <= 100000:
    print("Автомобіль у хорошому стані")
else:
    print("Автомобіль потребує перевірки")
