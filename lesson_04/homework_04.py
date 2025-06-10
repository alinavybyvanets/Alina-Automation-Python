adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
new_text_01 = adwentures_of_tom_sawer.replace("\n", " ")
# task 02 ==
""" Замініть .... на пробіл
"""
new_text_02 = new_text_01.replace("....", " ")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
new_text_03 = ' '.join(new_text_02.split())

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = new_text_03.count("h")
print (f"Літера h зустрічається в тексті {count_h} разів")
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = new_text_03.split()
count = 0
for word in words:
    if word[0].isupper():
        count= count + 1
print(f'В тексті {count} слів починається з великої літери')
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_index = new_text_03.find("Tom")
second_index = new_text_03.find("Tom", first_index +1)
print(f'Слово Tom зустрічається в тексті {second_index} разів')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in adwentures_of_tom_sawer.split(".")]
print(adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
four_sentence = adwentures_of_tom_sawer_sentences[3]
print(four_sentence)
small_register = four_sentence.lower()
print(small_register)



# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print('Є речення що починаэться з "By the time" ')
        print(sentence.strip())
        break
else:
    print ('Речень які починаються з "By the time" не знайдено ')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
last_sentence =  adwentures_of_tom_sawer_sentences[-1].strip()
words_last_sentence = last_sentence.split(" ")
count_words = len(words_last_sentence)
print(f'Кількість слів у останньому реченні {count_words}')
