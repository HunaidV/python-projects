#!/usr/bin/env python3

""" 
This module is for string characters with 
ascii character and digits
"""
import string

SHIFT = 3

choice = input("Would you like to encode or decode?")
WORD = input("Please enter text word")
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''

if choice == "encode":
    for letter in WORD:
        if letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            X = LETTERS.index(letter) + SHIFT
            ENCODED = ENCODED + LETTERS[X]
if choice == "decode":
    for letter in WORD:
        if letter ==  ' ':
            ENCODED = ENCODED + ' '
        else:
            X = LETTERS.index(LETTERS) - SHIFT
            ENCODED = ENCODED + LETTERS[X]
print(ENCODED)
