from ciphers import Cipher
from stringProcessing import process_string

lookup_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}


class Atbash(Cipher):

    def encrypt(self, text):
        """Encrypt text and return the result"""
        output = ""

        text = process_string(text)
        for char in text:
            if char.isspace():
                output += " "
            else:
                output += lookup_table[char]
        return output

    def decrypt(self, text):
        """Decrypt text and return the result"""
        output = ""

        text = process_string(text)
        for char in text:
            if char.isspace():
                output += " "
            else:
                output += lookup_table[char]
        return output
