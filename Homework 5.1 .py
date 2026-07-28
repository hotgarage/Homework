# ДЗ 5.1: Перевiрка iм'я змінної на допустимость використання
import keyword                                  # 1) підключаємо модуль


name = input("Введіть ім'я змінної: ")            #  Просимо ввести рядок для перевірки

first_is_digit = name[0].isdigit()                # Перевірка №1: перший символ — НЕ цифра

has_upper = False                                 # Перевірка №2: у рядку немає великих літер
for char in name:
    if char.isupper():                           # якщо знайшли велику літеру
        has_upper = True
        break                                    # далі можна не шукати

has_invalid = False                              # Перевірка №3: кожен символ — маленька літера, цифра або _
for char in name:
    if not (char.islower() or char.isdigit() or char == "_"):
        has_invalid = True                      # знайшли пробіл, !, @ або інше
        break

is_reserved = name in keyword.kwlist            #  Перевірка №4: ім'я не є зарезервованим словом Python

has_double_underscore = name.find("__") != -1   # Перевірка №5: немає двох підкреслень підряд

result = (not first_is_digit                    # Підсумок: True, якщо ВСІ перевірки пройдені
          and not has_upper
          and not has_invalid
          and not is_reserved
          and not has_double_underscore)

print(result)