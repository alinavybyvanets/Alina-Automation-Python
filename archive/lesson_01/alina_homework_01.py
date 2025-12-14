# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
    if True:
print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print (f"Apples: {apples}\nBanana: {banana}")

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр фігури: {perimetery}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
yablyni = 4
grushi = yablyni + 5
slyvy = yablyni - 2
vsi_dereva = yablyni + grushi + slyvy
print(f"У саду посадили {yablyni} яблуні, {grushi} груш, {slyvy}сливи.")
print(f"Скільки всього дерев посадили в саду?")
print(f"Всього посадили {vsi_dereva} дерев")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperatura_do_obidy = 5
temperatura_pislia_obidy = temperatura_do_obidy - 10
temperatura_nadvechir = temperatura_pislia_obidy + 4
print(f"До обіду температура повітря була {temperatura_do_obidy} градусів.")
print(f"Після обіду температура була {temperatura_pislia_obidy} градусів.")
print(f"Надвечір температура стала {temperatura_nadvechir} градусів")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
vsi_hlopchyky = 24
vsi_divchatka = vsi_hlopchyky // 2
siogodni_hlophykiv = vsi_hlopchyky - 1
siogodni_divchatok = vsi_divchatka - 2
siogodni_ditok = siogodni_divchatok + siogodni_hlophykiv
print(f"Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - {vsi_divchatka}")
print(f"1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.")
print(f"Cьогодні {siogodni_ditok} дітей у театральному гуртку")


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
knyga_1 = 8
knyga_2 = knyga_1 + 2
knyga_3 = (knyga_1 + knyga_2) / 2
vsi_knygy = knyga_1 + knyga_2 + knyga_3
print(f"Перша книжка коштує 8 грн., друга книжка дорожче на 2 грн і  коштує {knyga_2} грн, а третя коштує як половина вартості першої та другої разом - {knyga_3} грн")
print(f'Якщо всі книги  купити по одному примірнику, то вони будуть коштувать {vsi_knygy} грн.')