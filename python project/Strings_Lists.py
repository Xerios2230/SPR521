# Рядки. Списки
# Частина 2

# 1
chusla = input("Введіть список цілих чисел: ")

parne = 0
neparne = 0

for char in chusla.split():
    num = int(char)
    if num % 2 == 0:
        parne += 1
    else:
        neparne += 1

print(f"Кількість парних чисел: {parne}")
print(f"Кількість непарних чисел: {neparne}")


# 2
chusla = input("Введіть список цілих чисел: ")
num = int(chusla.split)
print(f"Найбільше число це: {max(num)}")
print(f"Найменьше число це: {min(num)}")


# 3
chusla = input("Введіть список цілих чисел: ")
nums = [int(x) for x in chusla.split()]

negative_nums = [x for x in nums if x < 0]
positive_nums = [x for x in nums if x > 0]

print(f"Найбільше від'ємне число це: {max(negative_nums)}")
print(f"Найменьше додатнє число це: {min(positive_nums)}")


# 4
chusla = input("Введіть список цілих чисел: ")
deuake_chuslo = int(input("Введіть деяке число: "))
result = ""
for char in chusla.split():
    num = int(char)
    if num > deuake_chuslo:
        result += str(num) + " "
print(result)


# 5
vuraz = input("Введіть арифметичний вираз (наприклад 23+12): ")

for op in ['+', '-', '*', '/']:
    if op in vuraz:
        parts = vuraz.split(op)
        num1 = float(parts[0])
        num2 = float(parts[1])
        operator = op
        break

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

print("Результат:", result)


# 6
nums = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))

non_negative = [x for x in nums if x >= 0]

non_negative.sort()

result = []
index = 0

for x in nums:
    if x < 0:
        result.append(x)
    else:
        result.append(non_negative[index])
        index += 1

print("Результат:", *result)



# Рядки. Списки
# Частина 1

# 1
text = input("Введіть текст: ")

count = text.count('.') + text.count('!') + text.count('?')

print("Кількість речень:", count)


# 2
import string

s = input("Введіть рядок: ")

s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())

if s_clean == s_clean[::-1]:
    print("Це паліндром")
else:
    print("Це не паліндром")


# 3
reserved = {"python", "java", "c++"}
text = input("Введіть текст: ")

words = text.split()

result_words = []
for w in words:
    if w.lower() in reserved:
        result_words.append(w.upper())
    else:
        result_words.append(w)

print(" ".join(result_words))


# 4
str = input("Введіть рядок: ")
c1 = input("Введіть перший символ: ")
c2 = input("Введіть другий символ: ")

i1 = str.find(c1)
i2 = str.find(c2)

if i1 != -1 and i2 != -1 and i1 < i2:
    result = str[:i1] + str[i2+1:]
else:
    result = str

print("Результат:", result)


# 5
text = input("Введіть текст: ")
chars = input("Введіть символи: ")

words = text.split()
result_words = []

for w in words:
    if not any(ch in w for ch in chars):
        result_words.append(w)

print(" ".join(result_words))


# 6
text = input("Введіть текст: ")

words = text.split()
words.reverse()

print(" ".join(words))
