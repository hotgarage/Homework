#  ДЗ 5.3: Hashtag
import string                                           # Імпортуємо модуль для string.punctuation

text = input("Введіть рядок: ")

for char in string.punctuation:                         # Замінюємо всі символи пунктуації на пробіли
    text = text.replace(char, ' ')                 # (так зручніше потім розділити текст на слова)

words = text.split(' ')                                 # Розділяємо рядок на окремі слова

cleaned_words = []                                      # новий список для "почищених" слів
for word in words:
    if word != '':                                      # пропускаємо порожні (від подвійних пробілів)
        cleaned_words.append(word.capitalize())         # додаємо слово з великою першою літерою

hashtag_inner = ''                                      # cкладаємо всі слова разом в один рядок
for word in cleaned_words:
    hashtag_inner += word

hashtag = '#' + hashtag_inner

if len(hashtag) > 140:                                  # Якщо довжина більше 140 символів — обрізаємо
    hashtag = hashtag[:140]
print(hashtag)