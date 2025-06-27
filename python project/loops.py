# Цикли 1
# 1
start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))
for i in range(start,finish + 1 ):
    if i % 7 == 0:
        print(i)
    

# 2
start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))
for i in range(start, finish + 1):
    print(i)
for i in range(finish, start - 1, -1):
    print(i)

# 3
start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))
for i in range(start, finish + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)
    i += 1

# 4
start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))
interval = int(input("Введіть інтервал: "))
poradok = int(input("Введіть у якомк порядку 1 - звичайний, 2 - зворотній: "))
match poradok:
    case 1:
        for i in range(start, finish + 1, interval):
            print(i)
    case 2:
        for i in range(finish, start - 1, -interval):
            print(i)

# 5
start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))
suma = 0
if start < finish:
    for i in range(start, finish + 1):
        if i % 4 == 0 and i % 6 != 0:
            suma += i

elif start > finish:
    for i in range(finish, start + 1):
        if i % 4 == 0 and i % 6 != 0:
            suma += i

if suma == 0:
     print("таких чисел немає")
else:
    print(suma)

# 6
a = int(input("Введіть число: "))
n = int(input("Введіть ступінь піднесеня: "))
an = 1
for i in range(1, n + 1):
        an = an * a
print(an)


# Цикли 2
# 1
start = int(input("Введіть початок діапазону: "))
finish = int(input("Введіть кінець діапазону: "))

even_sum = 0
even_count = 0

odd_sum = 0
odd_count = 0

mult9_sum = 0
mult9_count = 0

for i in range(start, finish + 1):
    if i % 2 == 0:
        even_sum += i
        even_count += 1
    if i % 2 != 0:
        odd_sum += i
        odd_count += 1
    if i % 9 == 0:
        mult9_sum += i
        mult9_count += 1

print("Сума парних:", even_sum)
print("Середнє парних:", even_sum / even_count)

print("Сума непарних:", odd_sum)
print("Середнє непарних:", odd_sum / odd_count)

print("Сума кратних 9:", mult9_sum)
print("Середнє кратних 9:", mult9_sum / mult9_count)

# 2
length = int(input("Введіть довжину лінії: "))
symbol = input("Введіть символ: ")

for i in range(length):
    print(symbol)

# 3
while True:
    num = int(input("Введіть число: "))
    if num == 7:
        print("Good bye!")
        break
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

# 4
sum_numbers = 0
max_number = None
min_number = None

while True:
    num = int(input("Введіть число: "))
    
    if num == 7:
        print("Good bye!")
        break

    sum_numbers += num

    if max_number is None or num > max_number:
        max_number = num

    if min_number is None or num < min_number:
        min_number = num

print("Сума чисел:", sum_numbers)
print("Максимальне число:", max_number)
print("Мінімальне число:", min_number)

# 5
n = int(input("Введіть ціле число N: "))

if n <= 1:
    print("Число має бути більшим за 1")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"Число {n} не є простим")
            break
    else:
        print(f"Число {n} є простим")

# 6
n = int(input("Введіть ціле число N: "))

a, b = 0, 1
found = False

while a <= n:
    if a == n:
        found = True
        break
    a, b = b, a + b

if found:
    print(f"Число {n} належить послідовності Фібоначчі")
else:
    print(f"Число {n} не належить послідовності Фібоначчі")