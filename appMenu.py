import sys
from keywordCiph import KeywordCipher
from atbash import Atbash
from affine import Affine
from affine import a_possible_values
from affine import check_a_factor

encrypt_decrypt_prompt = "WELCOME TO SECRET MESSAGES\n\nType encrypt for encryption or decrypt for decryption\n"
cipher_prompt = "Please choose cipher algorithm\nType Keyword, Atbash or Affine\n" \
                "Press any other key for exiting\n"
user_input_encrypt__prompt = "Provide the string you want to hide\n"
user_input_decrypt__prompt = "Provide the string you want to decrypt\n"
a_factor_prompt = "Provide a factor\n"
b_factor_prompt = "Provide b factor\n"

encrypt = "ENCRYPT"
decrypt = "DECRYPT"
cipher_keyword = "KEYWORD"
cipher_atbash = "ATBASH"
cipher_affine = "AFFINE"


def app_menu():
    """Application menu"""
    enc_dec_choice = input(encrypt_decrypt_prompt).upper()
    if enc_dec_choice != encrypt and enc_dec_choice != decrypt:
        sys.exit()

    algorithm_choice = input(cipher_prompt).upper()

    if algorithm_choice == cipher_keyword:
        keyword_obj = KeywordCipher(input("PROVIDE KEYWORD\n"))
        if enc_dec_choice == encrypt:
            encryption_res = keyword_obj.encrypt(input(user_input_encrypt__prompt))
        else:
            decryption_result = keyword_obj.decrypt(input(user_input_decrypt__prompt))
    elif algorithm_choice == cipher_atbash:
        atbash_obj = Atbash()
        if enc_dec_choice == encrypt:
            encryption_res = atbash_obj.encrypt(input(user_input_encrypt__prompt))
        else:
            decryption_result = atbash_obj.decrypt(input(user_input_decrypt__prompt))
    elif algorithm_choice == cipher_affine:
        affine_obj = Affine()
        print("\nValid values for a factor: {0}".format(a_possible_values))
        a = check_a_factor(int(input(a_factor_prompt)))
        b = int(input(b_factor_prompt))
        if enc_dec_choice == encrypt:
            encryption_res = affine_obj.encrypt(input(user_input_encrypt__prompt), a, b)
        else:
            decryption_result = affine_obj.decrypt(input(user_input_decrypt__prompt), a, b)
    else:
        sys.exit()

    (print("ENCRYPTED STRING: {0}".format(encryption_res)) if enc_dec_choice == encrypt else
     print("DECRYPTED STRING: {0}".format(decryption_result)))


if __name__ == '__main__':
    app_menu()

