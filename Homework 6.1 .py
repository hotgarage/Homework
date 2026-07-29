import string

user_input = input("Введите две буквы через дефис: ")

dash_position = user_input.find("-")

start_letter = user_input[:dash_position]

end_letter = user_input[dash_position + 1:]

start_index = string.ascii_letters.find(start_letter)

end_index = string.ascii_letters.find(end_letter)

result = string.ascii_letters[start_index:end_index + 1]

print(result)