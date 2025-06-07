alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don't much care where ——" said Alice.\n'
    '"Then it doesn't matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
vsi_symvoly_apostrophe = alice_in_wonderland.count("'")
print(f'Кількість символів апострофа - {vsi_symvoly_apostrophe}')
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_square = 436_402
azov_sea_square = 37_800
all_sea_square = black_sea_square + azov_sea_square
print(f'Площа Чорного моря становить {black_sea_square} км2, а площа Азовського моря становить {azov_sea_square} км2.')
print(f'Чорне та Азовське моря разом займають площу {all_sea_square} км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
vsi_sklady = 375_291
sklad_1_and_2 = 250_449
sklad_2_and_3 = 222_950
# x=товари на першому складі
# y=товари на другому складі
# z=товари на третьому складі
y = sklad_1_and_2 + sklad_2_and_3 -  vsi_sklady
x = sklad_1_and_2 - y
z = sklad_2_and_3 - y
print(f'Мережа супермаркетів має 3 склади, де всього розміщено {vsi_sklady} товарів')
print(f'На першому та другому складах перебуває {sklad_1_and_2} товарів')
print(f'На другому та третьому – {sklad_2_and_3} товарів')
print(f'Товарів на першому складі - {x}')
print(f'Товарів на другому складі - {y}')
print(f'Товарів на третьому складі - {z}')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

mountly_payment = 1179
number_of_payments = 18
total_cost = mountly_payment * number_of_payments
print(f'Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами».')
print(f'Відомо, що сплачувати необхідно буде півтора року, а це - {number_of_payments} місяців, по {mountly_payment} грн/місяць ')
print(f'Загальна вартість комп`ютера {total_cost} грн')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f'a) 8019 % 8 = {a}')
print(f'b) 9907 % 9 = {b}')
print(f'c) 2789 % 5 = {c}')
print(f'd) 7248 % 6 = {d}')
print(f'e) 7128 % 5 = {e}')
print(f'f) 19224 % 9 = {f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza = 4 * 274
medium_pizza = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_cost = big_pizza + medium_pizza + juice + cake + water
print(f'Іринка, готуючись до свого дня народження, склала список того, що їй потрібно замовити:')
print(f'4 великих піцци на {big_pizza} грн')
print(f'2 середніх піцци на {medium_pizza} грн')
print(f'4 соки на  {juice} грн')
print(f'1 торт на {cake} грн')
print(f'3 води  на {water} грн')
print(f'Всього їй знадибиться {total_cost} грн')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?

"""
all_photos = 232
photos_on_page = 8
all_pages = (all_photos + photos_on_page - 1) // photos_on_page
print(
    'Ігор займається фотографією.\n'
    'Він вирішив зібрати всі свої 232 фотографії та вклеїти в альбом.\n'
    'На одній сторінці може бути розміщено щонайбільше 8 фото.\n'
)
print(f'Йому знадобиться {all_pages} сторінок')


# task 10
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
distance_between_places = 1600
fuel_per_100_km = 9
capacity_of_gasoline_tank = 48
gasoline_for_trip = (distance_between_places / 100)  * fuel_per_100_km
number_of_filling_stations = int((gasoline_for_trip + capacity_of_gasoline_tank -1) /capacity_of_gasoline_tank)
print(
    f'Родина зібралася в автомобільну подорож із Харкова в Будапешт.\n'
    f'Відстань між цими містами становить 1600 км.\n'
    f'Відомо, що на кожні 100 км необхідно 9 літрів бензину.\n'
    f'Місткість баку становить 48 літрів\n'
    f'Для такої подорожі знадобиться {gasoline_for_trip} літрів бензину\n'
    f'Родині необхідно заїхати на заправку під час цієї подорожі {number_of_filling_stations} рази'
)