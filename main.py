"""
main.py
-------
Entry point for the Basic Encryption & Decryption tool.
Handles all user interaction (menus, input, output).
The actual encryption/decryption logic lives in cipher.py.
"""

from cipher import (
    caesar_encrypt,
    caesar_decrypt,
    caesar_brute_force,
    vigenere_encrypt,
    vigenere_decrypt,
)


def get_int_input(prompt: str) -> int:
    """Keep asking until the user enters a valid integer."""
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.\n")


def caesar_menu():
    print("\n--- Caesar Cipher ---")
    text = input("Enter your text: ")
    shift = get_int_input("Enter shift value (e.g. 3): ")

    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"\nOriginal text : {text}")
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")

    show_brute = input("\nWant to see a brute-force attack demo (no key needed)? (y/n): ")
    if show_brute.lower() == "y":
        print("\n--- Brute Force: trying all 25 possible shifts ---")
        for shift_value, guess in caesar_brute_force(encrypted):
            print(f"Shift {shift_value:2d}: {guess}")
        print("\nThis is why Caesar cipher is considered weak: "
              "no computing power needed, just 25 quick guesses!")


def vigenere_menu():
    print("\n--- Vigenere Cipher ---")
    text = input("Enter your text: ")
    keyword = input("Enter a keyword (letters only, e.g. 'lemon'): ")

    encrypted = vigenere_encrypt(text, keyword)
    decrypted = vigenere_decrypt(encrypted, keyword)

    print(f"\nOriginal text : {text}")
    print(f"Encrypted text: {encrypted}")
    print(f"Decrypted text: {decrypted}")


def main():
    print("=== Basic Encryption & Decryption Tool ===")

    while True:
        print("\nChoose an option:")
        print("1. Caesar Cipher")
        print("2. Vigenere Cipher")
        print("3. Quit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            caesar_menu()
        elif choice == "2":
            vigenere_menu()
        elif choice == "3":
            print("Exiting. Stay secure!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
