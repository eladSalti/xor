import string
import itertools
import re
import nltk


def xor_decrypt(encrypted_text, key):
    decrypted_text = ""
    key = key.encode('utf-8')  # Convert key to bytes using UTF-8 encoding

    for i in range(len(encrypted_text)):
        # Get the i-th byte from encrypted_text
        encrypted_byte = encrypted_text[i]

        # Get the i-th byte from key using modular arithmetic
        key_byte = key[i % len(key)]

        # XOR the two bytes to get the decrypted byte
        decrypted_byte = encrypted_byte ^ key_byte

        # Convert the decrypted byte to a character using ASCII encoding
        decrypted_char = chr(decrypted_byte)

        # Add the decrypted character to the decrypted text
        decrypted_text += decrypted_char

    return decrypted_text


def guess_key(encrypted_text, key_size):
    # Check if encrypted_text length is at least key_size
    if len(encrypted_text) < key_size:
        raise ValueError(f"Error: key size ({key_size}) is larger than encrypted text size ({len(encrypted_text)})")

    # Check if encrypted_text is a list of integers
    if not all(isinstance(i, int) for i in encrypted_text):
        raise ValueError("Error: encrypted_text must be a list of integers")
    # Check if the key size is larger than 0
    if key_size == 0:
        raise ValueError("Key size cannot be zero")

    matches = []

    for key in itertools.product(string.ascii_lowercase, repeat=key_size):
        # Convert key tuple to string
        key_str = ''.join(key)

        # Decrypt the encrypted text using the current key
        decrypted_text = xor_decrypt(encrypted_text, key_str)

        # Check if the decrypted text contains only printable ASCII characters
        if all(c in string.printable for c in decrypted_text):
            # Add the key and decrypted text to the matches list
            matches.append((key_str, decrypted_text))

    return matches


def filter_matches(matches):
    filtered_matches = []
    for key, decrypted_text in matches:
        # Split decrypted text into words
        words = re.findall(r'\w+', decrypted_text)

        # Count the number of English words
        english_word_count = 0
        for word in words:
            if word.isalpha() and word.lower() in english_words:
                english_word_count += 1

        # Check if the text is mostly in English
        if len(words) > 0 and english_word_count / len(words) > 0.5:
            filtered_matches.append((key, decrypted_text))

    return filtered_matches


english_words = set(word.lower() for word in nltk.corpus.words.words())
