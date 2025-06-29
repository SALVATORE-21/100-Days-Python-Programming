"""
Topics covered:
1.Lists
2.Loops

"""


import string
import random
# List of alphabets (a-z, A-Z)
alphabets = list(string.ascii_letters)  # ['a', 'b', ..., 'z', 'A', ..., 'Z']
# List of digits (0-9)
numbers = list(string.digits)  # ['0', '1', ..., '9']
# List of symbols (common special characters)
symbols = list("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~")

final_list = alphabets + numbers + symbols
length_of_password = int(input("Lenght of password u want!:"))
password = ''.join(random.choices(final_list,k=length_of_password))

print("The generated password is:",password)