# 1
n = input("Введіть список цифер/чисел: ")
list1 = [int(num) for num in n.split()]
print(f"Сума цих цифр/числ = {sum(list1)}")
print(f"Середнє арефметичне цих цифр/числ = {sum(list1)/len(list1)}")

# 2
n = input("Введіть список чисел: ")
dnum = int(input("Введіть цифру/число для пошуку: "))
list1 = [int(num) for num in n.split()]
print(f"Цю цифру/число згадано {list1.count(dnum)} разів")

# 3
n = input("Введіть список цифер/чисел: ")
list1 = [int(num) for num in n.split() if num > 0]
print(f"Сума цих цифр/числ = {sum(list1)}")

# 4
numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
even_indexes = [i for i, num in enumerate(numbers) if num % 2 == 0]
print("Індекси парних чисел:", even_indexes)

# 5
text = input("Введіть текст: ")
sentences = text.split('.')
sentences = [s.strip().capitalize() for s in sentences if s.strip()]
new_text = '. '.join(sentences)
if text.strip().endswith('.'):
    new_text += '.'

digits_count = sum(c in '0123456789' for c in text)
punctuation_symbols = '.,;:!?-()[]{}"\''
punctuation_count = sum(c in punctuation_symbols for c in text)
exclamation_count = text.count('!')

print("\nТекст з великої літери кожного речення:\n", new_text)
print("\nКількість цифр у тексті:", digits_count)
print("Кількість розділових знаків:", punctuation_count)
print("Кількість знаків оклику:", exclamation_count)

# 6
numbers = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))
unique_numbers = [num for num in numbers if numbers.count(num) == 1]
print("Список унікальних елементів:", unique_numbers)
