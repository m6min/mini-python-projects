def encrypt_text(text, shift):
    """ Shifts the given text for given key number in the alphabet """
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt_text(text, shift):
    """ Decrypting the password that is shifted (Negative shift)"""
    return encrypt_text(text, -shift)

def crack_message(text):
    """ This function tries all possible keys for the decrypted message"""
    for key in range(1,27):
        decrypted_text = decrypt_text(text, key)
        print(f"For key {key}, message: {decrypted_text}")

def main():
    """ main function for while loop"""
    print("\n--- ROT-CLI: Rotation Cipher Tool ---")
    while True:
        print("\n 1- Encrypt a text |"
              "2- Decrypt a message | 3- Crack a message (No need key value) | q- Quit")
        choice = input("Choice: ")

        if choice == 'q':
            print("Exiting...")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice!")
            continue

        text = input("Enter message: ")
        if choice == '3':
            crack_message(text)
            continue
        else:
            try:
                shift = int(input("Enter the key (Shift number): "))
            except ValueError:
                print("It must be a number!")
                continue

            if choice == '1':
                encrypted = encrypt_text(text, shift)
                print(f"\nEncrypted: {encrypted}")

            elif choice == '2':
                decrypted = decrypt_text(text, shift)
                print(f"\nDecrypted: {decrypted}")

if __name__ == "__main__":
    main()
