def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            offset = ord('A') if char.isupper() else ord('a')
            #Shift character and handle wrap-around
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text.append(encrypted_char)
        else:
            # If character is not a letter, don't encrypt it
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def encrypt():
    message = input("Enter the message to encrpt:")
    shift = int(input("Enter the shift value:"))
    encrypted_message = caesar_cipher(message,shift)
    print(f"Encrypted message: {encrypted_message}")

def decrypt():
    message = input("Enter the message to decrypt:")
    shift = int(input("Enter the shift value:"))
    # To decrypt, use the negative shift value
    decrypted_message = caesar_cipher(message,-shift)
    print(f"Decrypted message: {decrypted_message}")


def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choose an option (1/2/3):")

        if choice == '1':
            encrypt()
        elif choice == '2':
            decrypt()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 1,2,3.")

if __name__ == "__main__":
    main()