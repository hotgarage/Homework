# Константы
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60

total_seconds = int(input("Введите количество секунд: "))

days, remainder = divmod(total_seconds, SECONDS_IN_DAY)

hours, remainder = divmod(remainder, SECONDS_IN_HOUR)

minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

last_digit = days % 10
last_two_digits = days % 100

if last_two_digits in (11, 12, 13, 14):
    day_word = "днів"
elif last_digit == 1:
    day_word = "день"
elif last_digit in (2, 3, 4):
    day_word = "дні"
else:
    day_word = "днів"

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")