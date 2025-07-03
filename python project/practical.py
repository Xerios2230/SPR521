#practical
# 1
str = input("Введіть рядок: ")

bykvu = 0
chusla = 0

for char in str:
    if char.isalpha():
        bykvu += 1
    elif char.isdigit():
        chusla += 1

print(f"Кількість букв: {bykvu}")
print(f"Кількість цифр: {chusla}")


# 2
str = input("Введіть рядок: ")
symbol = input("Введіть символ для пошуку: ")

print(f"Кількіть повторення символу: {str.count(symbol)}")


# 3
str = input("Введіть рядок: ")

i = len(str) - 1

while i >= 0:
    str_reversed += str[i]
    i -= 1

print(str_reversed)


# 4 
str = input("Введіть рядок: ")
slovo = input("Введіть слово для пошуку: ")

print(f"Кількість повторення слова: {str.count(slovo)}")


# 5
str = input("Введіть рядок: ")
slovo = input("Введіть слово для пошуку: ")
zamina = input("Введіть слово для заміни: ")

print(f"Рядок після заміни: {str.replace(slovo, zamina)}")


# 6
str = input("Введіть рядок: ")

words = str.split()

max_word = words[0]

for word in words:
    if len(word) > len(max_word):
        max_word = word

print("Найдовше слово:", max_word)
