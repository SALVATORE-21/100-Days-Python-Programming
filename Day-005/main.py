alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "{", "]", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?", "`", "~"
]


import random
letter_count = int(input("How many letter u want in the final password: "))
symbol_count = int(input("How many symbols u want in the final password: "))
number_count = int(input("How many numbers u want in the final password: "))

password = ""
for i in range(1,letter_count):
    password += random.choice(alphabets)
for i in range(1,symbol_count):
    password += random.choice(symbols)
for i in range(1,number_count):
    password += random.choice(numbers)

print("The final password is:",password)

final_list = alphabets + symbols + numbers
length_of_password = int(input("Lenght of password u want!:"))
password = random.choices(final_list,length_of_password)
print("The final password is:",password)