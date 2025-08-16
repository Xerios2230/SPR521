# 1
try:
    price = float(input("Введіть вихідну ціну: "))
    discount = float(input("Введіть відсоток знижки: "))
    print(f"підсумкова ціна = {price - ((discount / 100) * price)}")
except ValueError:
    print("ValueError")
finally:
    print("end")

# 2
try:
    dollars = float(input("Введіть кількість доларів: "))
    kurs =  float(input("Введіть курс євро: "))
    if kurs <= 0:
        print("Курс обміну не може дорівнювати нулю")
    else:
        print(f"в євро = {dollars*kurs}")
except ValueError:
    print("ValueError")

# 3
try:
    grades = input("Введіть оцінки студентів через пробіл: ")
    grades_list = [float(i) for i in grades.split()]
    if len(grades_list) == 0:
        raise ZeroDivisionError
    print(f"Середнє значення = {sum(grades_list) / len(grades_list):.2f}")
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("Завершення обчислень.")

# 4
balance = 1000

try:
    amount = int(input("Введіть суму для зняття: "))
    if amount % 10 != 0 or amount > balance or amount <= 0:
        raise Exception("Некоректна сума для зняття")
    print(f"Знято: {amount} грн")
except ValueError:
    print("ValueError")
except Exception as e:
    print(e)
finally:
    print("Завершення транзакції.")

# 5
try:
    order = input("Введіть номер замовлення: ")
    if not (order.startswith("ORD") and order[3:].isdigit()):
        raise Exception("Неправильний формат номера замовлення")
    print("Номер прийнято")
except Exception as e:
    print(e)
finally:
    print("Завершення перевірки.")

# 6
try:
    numbers = input("Введіть числа через пробіл: ").split()
    result = []
    for i in numbers:
        try:
            result.append(float(i))
        except ValueError:
            print(f"Пропущено: {i}")
    if len(result) == 0:
        raise ZeroDivisionError
    print(f"Сума = {sum(result):.2f}, Середнє = {sum(result)/len(result):.2f}")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("Завершення обробки.")
