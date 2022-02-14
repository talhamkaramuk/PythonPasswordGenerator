import random

letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
          "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbol = ["!", "#", "$", "%", "&", "(", ")", "*", "-", ".", "/", "+", "_"]

print("Welcome to the password generator!")

number_of_letters = int(
    input("How many letters do you want in your password? "))

number_of_numbers = int(
    input("How many numbers do you want in your password? "))

number_of_symbols = int(
    input("How many symbols do you want in your password? "))

########### Easy Way #############

# password = ""

# for char in range(1, number_of_letters + 1):
#     password += random.choice(letter)
# for num in range(1, number_of_numbers + 1):
#     password += random.choice(number)
# for sym in range(1, number_of_symbols + 1):
#     password += random.choice(symbol)

# print("Your password is: " + password)

########## Hard Way ##########

password_list = []

for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letter))
for num in range(1, number_of_numbers + 1):
    password_list.append(random.choice(number))
for sym in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbol))
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print("Your password is: " + password)
