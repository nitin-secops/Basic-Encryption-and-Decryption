"""
cipher.py
---------
Core logic for encryption and decryption.
Two techniques implemented:
    1. Caesar Cipher   - shifts each letter by a fixed number
    2. Vigenere Cipher - shifts each letter using a repeating keyword
                         (stronger than Caesar, because the shift changes)

Kept separate from main.py so the logic can be tested and reused
independently of the CLI.
"""

import string

ALPHABET_SIZE = 26


def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypt text using a Caesar cipher with the given shift.
    Non-letter characters (spaces, numbers, punctuation) are left unchanged.
    """
    result = []
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') + shift) % ALPHABET_SIZE
            result.append(chr(shifted + ord('A')))
        elif char.islower():
            shifted = (ord(char) - ord('a') + shift) % ALPHABET_SIZE
            result.append(chr(shifted + ord('a')))
        else:
            # Leave spaces, digits, punctuation untouched
            result.append(char)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypt a Caesar-ciphered text.
    Decryption is just encryption with the opposite (negative) shift.
    """
    return caesar_encrypt(text, -shift)


def caesar_brute_force(text: str) -> list:
    """
    Try all 25 possible shifts and return every possible decryption.
    Demonstrates why Caesar cipher is weak: an attacker doesn't need
    the key, just 25 attempts to read the message.
    """
    return [(shift, caesar_decrypt(text, shift)) for shift in range(1, ALPHABET_SIZE)]


def vigenere_encrypt(text: str, keyword: str) -> str:
    """
    Encrypt text using a Vigenere cipher.
    Each letter of the text is shifted by the corresponding letter of the
    keyword (repeated as needed). Non-letters are left unchanged and do
    NOT consume a position in the keyword.
    """
    keyword = keyword.lower()
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            if char.isupper():
                shifted = (ord(char) - ord('A') + shift) % ALPHABET_SIZE
                result.append(chr(shifted + ord('A')))
            else:
                shifted = (ord(char) - ord('a') + shift) % ALPHABET_SIZE
                result.append(chr(shifted + ord('a')))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def vigenere_decrypt(text: str, keyword: str) -> str:
    """
    Decrypt a Vigenere-ciphered text using the same keyword.
    Works the same way as encryption but subtracts the shift instead.
    """
    keyword = keyword.lower()
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            if char.isupper():
                shifted = (ord(char) - ord('A') - shift) % ALPHABET_SIZE
                result.append(chr(shifted + ord('A')))
            else:
                shifted = (ord(char) - ord('a') - shift) % ALPHABET_SIZE
                result.append(chr(shifted + ord('a')))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)
