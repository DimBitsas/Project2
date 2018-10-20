from ciphers import Cipher
from stringProcessing import process_string

# m == 26 since we are using the English alphabet
m = 26

a_possible_values = {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

lookup_table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
                'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}


def check_a_factor(a):
    """Checks if a factor contains a valid value"""
    if a not in a_possible_values:
        raise ValueError("Not valid a factor")
    return a


class Affine(Cipher):
    def encrypt(self, text, a, b):
        """Encrypt text and return the result
           E(x) = ( ax + b ) mod m
        """
        output = ""

        text = process_string(text)
        for char in text:
            if char.isspace():
                output += " "
            else:
                char_code = (a*lookup_table[char] + b) % m
                for k, v in lookup_table.items():
                    if v == char_code:
                        break
                output += k
        return output

    def decrypt(self, text, a, b):
        """Decrypt text and return the result
           D(x) = a^-1 ( x - b ) mod m
        """
        output = ""

        text = process_string(text)
        count = 0
        a_inv = 0
        while count < m:
            flag = (a * count) % m
            if flag == 1:
                a_inv = count
                break;
            count = count + 1

        for char in text:
            if char.isspace():
                output += " "
            else:
                char_code = a_inv*(lookup_table[char]-b) % m
                for k, v in lookup_table.items():
                    if v == char_code:
                        break
                output += k
        return output

