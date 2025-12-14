# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    result = []
    while number * multiplier <= 25:
        result.append(f"{number} x {multiplier} = {number * multiplier}")
        multiplier += 1
    return result
if __name__ == '__main__':
    for number in multiplication_table(3):
        print(number)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_sum(a, b):
    return a + b
if __name__ == '__main__':
    num1 = int(input("Введіть перше число"))
    num2 = int(input("Введіть друге число"))
    result = add_sum(num1, num2)
    print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def  arefmetic(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    user_list = input("Ведіть числа  через пробіл")
    numbers = list(map(int, user_list.split()))
    result = arefmetic(numbers)
    if result is not None:
        print(f'Середнє арифметичне цього списку {result}')
    else:
        print("Список пустий, введіть хоча б одне значення")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(znachennia):
    if len(znachennia) == 0:
        return None
    return znachennia[::-1]
if __name__ == '__main__':
    user_text = input("Введіть рядок:")
    result = reverse_string(user_text)
    if result is not None:
        print(f'Рядок в зворотньому порядку {result}')
    else:
        print("Рядок пустий")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def words_list(words):
    if len(words) == 0:
        return None
    return max(words, key = lambda x: len(x))
if __name__ == '__main__':
    user_text = input("Введіть текст:")
    words = user_text.split()
    result = words_list(words)
    if result is not None:
        print(f'Найдовше слово в рядку {result}')
    else:
        print("Рядок пустий")

