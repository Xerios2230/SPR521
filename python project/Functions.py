# Функції
# Частина 1
# 1
def print_quote():
    print('"Don\'t compare yourself with anyone in this world… ')
    print('    if you do so, you are insulting yourself."')
    print('        Bill Gates')

print_quote()

# 2
def print_even_numbers(start, end):
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num)

print_even_numbers(3, 15)

# 3
def print_square(side, symbol, filled):
    for i in range(side):
        if filled or i == 0 or i == side - 1:
            print(symbol * side)
        else:
            print(symbol + ' ' * (side - 2) + symbol)

print_square(5, '*', True)
print()
print_square(5, '#', False)

# 4
def min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)

result = min_of_five(10, 3, 5, 8, 2)
print("Мінімальне число:", result)

# 5
def count_digits(number):
    return len(str(abs(number)))

print("Кількість цифр:", count_digits(3456))
print("Кількість цифр:", count_digits(-98765))

# 6
def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

print(is_palindrome(123321))
print(is_palindrome(546645))
print(is_palindrome(421987))



# Функції
# Частина 2
# 1
def range_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

print(range_sum(25, 5))

# 2
def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(product_of_list([1, 2, 3, 4]))

# 3
def min_in_list(numbers):
    return min(numbers)

print(min_in_list([7, 2, 9, -4, 0]))

# 4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers):
    return sum(1 for num in numbers if is_prime(num))

print(count_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 5
def remove_and_count(numbers, value):
    original_length = len(numbers)
    numbers[:] = [x for x in numbers if x != value]
    return original_length - len(numbers)

lst = [3, 1, 2, 3, 4, 3, 5]
count = remove_and_count(lst, 3)
print("Кількість видалених:", count)
print("Оновлений список:", lst)

# 6
def merge_lists(list1, list2):
    return list1 + list2

print(merge_lists([1, 2], [3, 4]))

# 7
def power_list(numbers, exponent):
    return [x ** exponent for x in numbers]

print(power_list([2, 3, 4], 3))