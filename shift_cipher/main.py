import streamlit as st

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
    for key in range(1, 27):
        decrypted_text = decrypt_text(text, key)
        st.write(f"For key {key}, message: {decrypted_text}")

st.title("ROT-CLI: Rotation Cipher Tool")

choice = st.radio("Choice:", ["Encrypt a text", "Decrypt a message", "Crack a message (No need key value)"])

text = st.text_input("Enter message:")
shift = 1
if choice != "Crack a message (No need key value)":
    shift = st.number_input("Enter the key (Shift number):", min_value=1, max_value=25, step=1)

if st.button("Run"):
    if choice == "Crack a message (No need key value)":
        crack_message(text)
    elif choice == "Encrypt a text":
        encrypted = encrypt_text(text, shift)
        st.write(f"Encrypted: {encrypted}")
    elif choice == "Decrypt a message":
        decrypted = decrypt_text(text, shift)
        st.write(f"Decrypted: {decrypted}")
