# 🔐 ROT-CLI: Rotation Cipher Tool

A Python-based Command Line Interface (CLI) tool for encrypting and decrypting text using the **Caesar Cipher** (Rotation Cipher) algorithm. It also includes a **Brute Force Cracker** feature to decode messages without a key.

## 🚀 Features

* **Encryption:** Shifts characters by a specified key using ASCII manipulation.
* **Decryption:** Reverses the shift to reveal the original message.
* **Brute Force Cracker:** Automatically attempts all 26 possible shifts to break a code without the key.
* **Smart Handling:** Preserves case (Upper/Lower) and ignores non-alphabetic characters (numbers, symbols).

## Technical Details

* **Language:** Python 3.x
* **Core Concepts:**
    * **ASCII Manipulation:** Uses `ord()` and `chr()` for character-to-integer conversion.
    * **Modulo Arithmetic:** Uses `% 26` to handle alphabet wrapping.

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd python-mini-projects/shift_cipher
    ```
2.  Run the script:
    ```bash
    python main.py
    ```

## Usage Example

```text
--- ROT-CLI: Rotation Cipher Tool ---

1- Encrypt a text | 2- Decrypt a message | 3- Crack a message (No need key value) | q- Quit
Choice: 1
Enter message: Hello World
Enter the key (Shift number): 1

🔒 Encrypted: Ifmmp Xpsme