# Функції
# Частина 2

# 1
def dobytokChusel():
    start = int(input("Введіть початок діапазону: "))
    finish = int(input("Введіть кінець діапазону: "))
    dob = 1
    if start > finish:
        for i in range(start, finish - 1, -1):
            dob *= i
    else:
        for i in range(start, finish + 1):
            dob *= i
    print(f"Добуток діапазону = {dob}")

dobytokChusel()

# 2
def maxx(list = [1,24,25,57,214,742,2434,35]):
    maxNumber = 0
    for i in list:
        if i > maxNumber:
            maxNumber = i
    print(f"Максимальне число зі списку це {maxNumber}")

maxx()

# 3
def summ(list = [1,32,25,25,36,16,364,356,3]):
    suma = 0
    for num in list:
        suma += num
    print(suma)

summ()

# 4
def potato(list = [1,5,2,6,7,4,-2,-45,-36,-3,-6,-7]):
    parni = 0
    neparni = 0
    dodatni = 0
    vidyemni = 0
    for i in list:
        if i % 2 == 0:
            parni += 1
        if i % 2 != 0:
            neparni += 1
        if i > 0:
            dodatni += 1
        if i < 0:
            vidyemni += 1

    print(parni, neparni, dodatni, vidyemni)

# 5
def tomato(list2 = [1,4,6,35,85,25,58,89]):
    print(list(reversed(list2)))

# 6
import math

def shashlik(numbers):
    result = []
    for num in numbers:
        if num >= 0:
            result.append(math.factorial(num))
        else:
            result.append(None)
    return result

# 7
def ananas(numbers = [1,53,36,547,357,7456,2465346,897]):
    max_num = max(numbers)
    fib = [0, 1]
    while fib[-1] < max_num:
        fib.append(fib[-1] + fib[-2])
    return [x for x in numbers if x in fib]
