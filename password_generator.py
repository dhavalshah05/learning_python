import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generating random letters
for index in range(0, nr_letters):
    random_number = random.randint(0, len(letters) - 1)
    random_letter = letters[random_number]
    password.append(random_letter)

# Generating random symbols
for index in range(0, nr_symbols):
    random_number = random.randint(0, len(symbols) - 1)
    random_symbol = symbols[random_number]
    password.append(random_symbol)

# Generating random numbers
for index in range(0, nr_numbers):
    random_number = str(random.randint(0, 9))
    password.append(random_number)

random.shuffle(password)
print("".join(password))

