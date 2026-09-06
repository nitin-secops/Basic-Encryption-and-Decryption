# Basic Encryption & Decryption

A Python command-line tool that implements two classic encryption techniques — **Caesar Cipher** and **Vigenere Cipher** — to encrypt and decrypt text.

Built as Project 2 for the Cyber Security Internship at **Decode Labs**.

## Project Structure

```
basic-encryption-decryption/
├── main.py              # CLI entry point (menus, user interaction)
├── cipher.py            # Core encryption/decryption logic
├── README.md
└── tests/
    └── test_cipher.py   # Unit tests for the core logic
```

## Features

- **Caesar Cipher** — encrypt/decrypt text using a fixed numeric shift
- **Vigenere Cipher** — encrypt/decrypt text using a repeating keyword (stronger, since the shift changes per letter)
- **Brute-force demo** — tries all 25 possible Caesar shifts to recover text without knowing the key, demonstrating why Caesar cipher alone is weak
- Preserves spaces, numbers, and punctuation — only letters are shifted
- Handles both uppercase and lowercase letters correctly

## How It Works

**Caesar Cipher**: every letter is shifted forward in the alphabet by a fixed number (the "shift" or "key"). For example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on, wrapping around from `Z` back to `A`.

**Vigenere Cipher**: instead of one fixed shift, a keyword is repeated across the message, and each letter of the keyword determines the shift for the corresponding letter of the text. This makes the cipher significantly harder to break than Caesar, since the same letter can be encrypted differently depending on its position.

## Usage

```bash
python3 main.py
```

You'll see a menu:
```
1. Caesar Cipher
2. Vigenere Cipher
3. Quit
```

### Example (Caesar Cipher)

```
--- Caesar Cipher ---
Enter your text: Hello World
Enter shift value (e.g. 3): 5

Original text : Hello World
Encrypted text: Mjqqt Btwqi
Decrypted text: Hello World
```

### Example (Vigenere Cipher)

```
--- Vigenere Cipher ---
Enter your text: Attack at Dawn
Enter a keyword (letters only, e.g. 'lemon'): lemon

Original text : Attack at Dawn
Encrypted text: Lxfopv ef Rnhr
Decrypted text: Attack at Dawn
```

## Running the Tests

```bash
cd tests
python3 test_cipher.py
```

All 7 tests should print `PASS`.

## Skills Demonstrated

- Encryption concepts (substitution ciphers, keys, shift-based logic)
- String and character manipulation (ASCII values, modular arithmetic)
- Logic building for encode/decode symmetry
- Data protection basics and understanding cipher weaknesses (brute force)

## Author

Nitin Yadav — Cyber Security Intern at Decode Labs
