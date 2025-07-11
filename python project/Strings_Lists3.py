# 1
numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1

print("Кількість елементів:", count)

# 2
numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
unique = [x for x in numbers if numbers.count(x) == 1]
print("Елементи, що зустрічаються один раз:", unique)

# 3
numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
max_seq = []
current_seq = []
for i in range(len(numbers)):
    if not current_seq or numbers[i] > current_seq[-1]:
        current_seq.append(numbers[i])
    else:
        if len(current_seq) > len(max_seq):
            max_seq = current_seq
        current_seq = [numbers[i]]

if len(current_seq) > len(max_seq):
    max_seq = current_seq

print("Довжина послідовності:", len(max_seq))
print("Послідовність:", max_seq)

# 4
numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
n = int(input("Введіть кількість позицій для зсуву: "))
n = n % len(numbers)
shifted = numbers[-n:] + numbers[:-n]
print("Зсунутий список:", shifted)

# 5
list1 = list(map(int, input("Введіть перший список цілих чисел: ").split()))
list2 = list(map(int, input("Введіть другий список цілих чисел: ").split()))

combined = list1 + list2
print("Об'єднаний список:", combined)

combined_unique = list(set(combined))
print("Об'єднаний без повторень:", combined_unique)

common = list(set(list1) & set(list2))
print("Спільні елементи:", common)

unique = list(set(list1) ^ set(list2))
print("Унікальні елементи кожного списку:", unique)

min_max = [min(list1), max(list1), min(list2), max(list2)]
print("Мінімальні та максимальні значення:", min_max)

# 6
numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
numbers.sort()
result = []
while numbers:
    if numbers:
        result.append(numbers.pop(0))
    if numbers:
        result.append(numbers.pop(-1))

print("Відсортований список:", result)
