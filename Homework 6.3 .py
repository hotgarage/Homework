# Водим целое число

n = int(input("Введите число: "))

while n > 9:

    product = 1

    for digit_char in str(n):

        product = product * int(digit_char)

    n = product

#  n <= 9, виходим  из цикла
print(n)