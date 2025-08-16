import math, random

# 1
try:
    print(float(input("a: ")) / float(input("b: ")))
except ValueError: print("Не число")
except ZeroDivisionError: print("Ділення на 0")
finally: print("Готово\n")

# 2
arr=[10,20,30,40,50]
try: print(arr[int(input("Індекс: "))])
except ValueError: print("Не число")
except IndexError: print("Нема такого індексу")
finally: print("Готово\n")

# 3
try:
    print("Сума:", sum(map(float,input("Продажі: ").split())))
except ValueError: print("Помилка вводу")
finally: print("Готово\n")

# 4
try:
    n=float(input("Число: "))
    if n<0: raise Exception("Корінь від'ємного числа")
    print("√ =", math.sqrt(n))
except (ValueError,Exception) as e: print("Помилка:",e)
finally: print("Готово\n")

# 5
try:
    name,price,qty=input("Товар: ").split(",")
    print(f"{name.strip()} {float(price)}грн x{int(qty)}")
except ValueError: print("Формат невірний")
finally: print("Готово\n")

# 6
def connect(): 
    if random.choice([1,0]): return "Підключено!"
    raise ConnectionError
try: print(connect())
except ConnectionError: print("Не вдалося підключитися")
finally: print("Спробу завершено")
