# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
multiplication_table(3)



# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_sum(a, b):
    return a + b
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

user_text = input("Введіть текст:")
words = user_text.split()
result = words_list(words)
if result is not None:
    print(f'Найдовше слово в рядку {result}')
else:
    print("Рядок пустий")


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1
text_str1 = input("Введіть перший рядок")
text_str2 = input("Введіть другий рядок")
result = find_substring(text_str1, text_str2)
print(result)

"""str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1"""

# task 7
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?

"""
def all_pages(all_photos, photos_on_page):
    return (all_photos + photos_on_page - 1) // photos_on_page

all_photos = 232
photos_on_page = 8
result = all_pages(all_photos, photos_on_page)
print(f'Ігорю знадобиться {result} сторінок')
# task 8
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?

"""
def trip(distance_between_places, fuel_per_100_km, capacity_of_gasoline_tank):
    gasoline_for_trip = (distance_between_places / 100)  * fuel_per_100_km
    number_of_filling_stations = int((gasoline_for_trip + capacity_of_gasoline_tank -1) /capacity_of_gasoline_tank)
    return gasoline_for_trip, number_of_filling_stations
distance_between_places = 1600
fuel_per_100_km = 9
capacity_of_gasoline_tank = 48
gasoline_for_trip, number_of_filling_stations = trip(
    distance_between_places,
    fuel_per_100_km,
    capacity_of_gasoline_tank
)
print(
    f'Для такої подорожі знадобиться {gasoline_for_trip} літрів бензину\n'
    f'Родині необхідно заїхати на заправку під час цієї подорожі {number_of_filling_stations} рази'
)
# task 9
"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def computer(mountly_payment, number_of_payments):
   return  mountly_payment * number_of_payments
mountly_payment = 1179
number_of_payments = 18
result = computer(mountly_payment, number_of_payments)
print(f'Загальна вартість комп`ютера {result} грн')
# task 10
"""Площа Чорного моря становить 436 402 км2, 
а площа Азовськогоморя становить 37 800 км2. Яку площу займають Чорне та Азов-ське моря разом?
"""
def square(black_sea_square, azov_sea_square):
    return black_sea_square + azov_sea_square
black_sea_square = 436_402
azov_sea_square = 37_800
all_sea_square = square(black_sea_square, azov_sea_square)
print(f'Чорне та Азовське моря разом займають площу {all_sea_square} км2')

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції(task 7,8,9,10) що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""