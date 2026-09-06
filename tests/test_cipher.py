"""
test_cipher.py
---------------
Basic unit tests for cipher.py.
Run this file directly to see PASS/FAIL results for each test.
"""

import sys
import os

# Add the parent folder to the path so we can import cipher.py
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from cipher import (
    caesar_encrypt,
    caesar_decrypt,
    caesar_brute_force,
    vigenere_encrypt,
    vigenere_decrypt,
)


def test_caesar_roundtrip():
    original = "Hello, World!"
    encrypted = caesar_encrypt(original, 7)
    decrypted = caesar_decrypt(encrypted, 7)
    assert decrypted == original, "Decrypting should return the original text"


def test_caesar_changes_text():
    original = "abc"
    encrypted = caesar_encrypt(original, 3)
    assert encrypted == "def", "Shift of 3 should turn 'abc' into 'def'"


def test_caesar_wraps_around_alphabet():
    # 'z' shifted by 1 should wrap around to 'a'
    assert caesar_encrypt("z", 1) == "a", "Shift should wrap around from z to a"


def test_caesar_preserves_non_letters():
    original = "Hello, World! 123"
    encrypted = caesar_encrypt(original, 5)
    assert "," in encrypted and "!" in encrypted and "123" in encrypted, \
        "Punctuation and numbers should not be altered"


def test_caesar_brute_force_finds_original():
    original = "attackatdawn"
    encrypted = caesar_encrypt(original, 10)
    results = caesar_brute_force(encrypted)
    guesses = [guess for _, guess in results]
    assert original in guesses, "Brute force should recover the original among its guesses"


def test_vigenere_roundtrip():
    original = "Attack at Dawn"
    keyword = "lemon"
    encrypted = vigenere_encrypt(original, keyword)
    decrypted = vigenere_decrypt(encrypted, keyword)
    assert decrypted == original, "Decrypting should return the original text"


def test_vigenere_wrong_keyword_fails():
    original = "Attack at Dawn"
    encrypted = vigenere_encrypt(original, "lemon")
    decrypted_wrong = vigenere_decrypt(encrypted, "grape")
    assert decrypted_wrong != original, \
        "Decrypting with the wrong keyword should NOT recover the original text"


def run_all_tests():
    tests = [
        test_caesar_roundtrip,
        test_caesar_changes_text,
        test_caesar_wraps_around_alphabet,
        test_caesar_preserves_non_letters,
        test_caesar_brute_force_finds_original,
        test_vigenere_roundtrip,
        test_vigenere_wrong_keyword_fails,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test.__name__} -> {e}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed out of {len(tests)} tests")


if __name__ == "__main__":
    run_all_tests()
