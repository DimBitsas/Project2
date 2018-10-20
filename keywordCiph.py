from ciphers import Cipher
from stringProcessing import process_string
import re

# Contains all the letters of the english alphabet, uppercase
english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# This list will contain the new created "keyword alphabet"
# after the keyword is inserted by the user
keyword_alphabet = []


class KeywordCipher(Cipher):

    def __init__(self, key):
        if re.search('\d', key):
            raise ValueError("Keyword must be a string")
        else:
            self.key = key.upper()
            self.create_keyword_alphabet()

    def encrypt(self, text):
        """Encrypt text and return the result"""
        output = []
        text = process_string(text)
        for char in text:
            output.append(keyword_char(char))
        return ''.join(output)

    def decrypt(self, text):
        """Decrypt text and return the result"""
        output = []
        text = process_string(text)
        for char in text:
            output.append(english_char(char))
        return ''.join(output)

    def create_keyword_alphabet(self):
        """Create the keyword alphabet"""
        for char in self.key:
            keyword_alphabet.append(char)
        for char in english_alphabet:
            if char not in keyword_alphabet:
                keyword_alphabet.append(char)


def keyword_char(eng_char):
    """Takes a character as an argument and returns
       the equivalent keyword alphabet character
    """
    if eng_char in english_alphabet:
        return keyword_alphabet[english_alphabet.index(eng_char)]
    else:
        return" "


def english_char(key_char):
    """Takes a keyword character as an argument and returns
       the equivalent english alphabet character
    """
    if key_char in keyword_alphabet:
        return english_alphabet[keyword_alphabet.index(key_char)]
    else:
        return" "

