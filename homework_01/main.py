"""
Домашнее задание №1
Функции и структуры данных
"""

"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
"""


def power_numbers(*nums):
    squares = []
    for num in nums:
        squares.append(num * num)
    return squares


print(power_numbers(1, 2, 5, 7))



"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

first_list_of_numbers = [1, 2, 3]
second_list_of_numbers = [2, 3, 4, 5]
third_list_of_numbers = [1, 3, 2, 5, 6, 11, 20]


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def filter_numbers(nums, arg):
    if arg is ODD:
        odds = []
        odds = list(filter(lambda x: x % 2 == 1, nums))
        return odds
    if arg is EVEN:
        evens = []
        evens = list(filter(lambda x: x % 2 == 0, nums))
        return evens
    if arg is PRIME:
        primes = []
        for num in nums:
            if is_prime(num) is False:
                print('skip', num)
            if is_prime(num) is True:
                print('add', num)
                primes.append(num)
        return primes


print(filter_numbers(first_list_of_numbers, ODD))
print(filter_numbers(second_list_of_numbers, EVEN))
print(filter_numbers(third_list_of_numbers, PRIME))

