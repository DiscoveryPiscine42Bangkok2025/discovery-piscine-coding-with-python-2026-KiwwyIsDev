#!/usr/bin/env python3


text = input()

new_text = ""
for char in text:
    # print(char)
    if char.isalpha():
        if char.isupper():
            new_text += char.lower()
        elif char.islower():
            new_text += char.upper()
    else:
        new_text += char
print(new_text)