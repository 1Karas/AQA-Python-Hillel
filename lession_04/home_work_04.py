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


# a = adwentures_of_tom_sawer.replace("\n", " ")
# print(a)

# # task 02 ==
# """ Замініть .... на пробіл
# """
# sentence = adwentures_of_tom_sawer.replace("....", " ")
# print(sentence)
# # task 03 ==
# """ Зробіть так, щоб у тексті було не більше одного пробілу між словами.
# """
#
# words = adwentures_of_tom_sawer.split()
# cleaned_text = "".join(words)
# wrapped_text = textwrap.fill(cleaned_text, width=80)
# print(wrapped_text)
#
#
# # task 04
# """ Виведіть, скількі разів у тексті зустрічається літера "h"
# """
# count = adwentures_of_tom_sawer.find('h')
# print(count)
#
# # task 05
# """ Виведіть, скільки слів у тексті починається з Великої літери?
# """
# uppercase_count = sum(map(str.isupper, adwentures_of_tom_sawer))
#
# print(f"Кількість заглавных букв: {uppercase_count}")
#
# # task 06
# """ Виведіть позицію, на якій слово Tom зустрічається вдруге
# """
#
# task 07
# """ Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences
# """
# sentence = adwentures_of_tom_sawer.replace("....", "")
# adwentures_of_tom_sawer_sentences = sentence.split('.')
# print(adwentures_of_tom_sawer_sentences)
#
# # task 08
# """ Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр.
# """
# sentence1 = adwentures_of_tom_sawer.replace("....", " ")
# sentences = re.split(r'(?<=[.!?])\s*', sentence1)
#
# if len(sentences) >= 4:
#     fourth_sentence = sentences[3].lower()
#     print(f"Четверте речення у нижньому регістрі: {fourth_sentence}")
# else:
#     print("В тексті недостатньо речень.")
#
# # task 09
# """ Перевірте чи починається якесь речення з "By the time".
# """
# if adwentures_of_tom_sawer.startswith("By the time"):
#     print("Рядок починається з 'By the time'")
# else:
#     print("Немає рядка який починається з 'By the time'")

# task 10
# """ Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
# """
# sentence2 = adwentures_of_tom_sawer.replace("....", " ")
# sentences = re.split(r'(?<=[.!?])\s+', sentence2)
#
# last_sentence = sentences[-1].strip()
# total = last_sentence.split()
# total_sum = len(total)
#
# print(f"Кількість слів в останньому реченні: {total_sum}")
