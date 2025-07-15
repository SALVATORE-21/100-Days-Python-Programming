"""
Topics covered
1. Functions
2. Position Arguments

"""

alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def encrypt(original_text, shift_amount):
    result = ''
    for char in original_text.lower():
        if char in alphabets:
            index = alphabets.index(char)
            shifted_index = (index + shift_amount) % 26
            result += alphabets[shifted_index]
        else:
            result += char
    return result


def decrypt(original_text, shift_amount):
    result = ''
    for char in original_text.lower():
        if char in alphabets:
            index = alphabets.index(char)
            shifted_index = (index - shift_amount) % 26
            result += alphabets[shifted_index]
        else:
            result += char
    return result

message = "hello world"
shift = 3

encrypted = encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)

