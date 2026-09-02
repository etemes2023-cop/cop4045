def caesar_cipher(text, shift):
    """Return text with its letters shifted by shift positions."""
    encrypted = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"

    for character in text:
        if character in uppercase:
            index = uppercase.index(character)
            encrypted += uppercase[(index + shift) % len(uppercase)]
        elif character in lowercase:
            index = lowercase.index(character)
            encrypted += lowercase[(index + shift) % len(lowercase)]
        else:
            encrypted += character

    return encrypted


def caesar_decipher(cyphertext, shift):
    """Return cyphertext decrypted by reversing a Caesar-cipher shift."""
    decrypted = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"

    for character in cyphertext:
        if character in uppercase:
            index = uppercase.index(character)
            decrypted += uppercase[(index - shift) % len(uppercase)]
        elif character in lowercase:
            index = lowercase.index(character)
            decrypted += lowercase[(index - shift) % len(lowercase)]
        else:
            decrypted += character

    return decrypted


def letter_frequency(text):
    """Return a dictionary counting each alphabetic letter in text."""
    frequencies = {}

    for character in text.lower():
        if character.isalpha():
            if character in frequencies:
                frequencies[character] += 1
            else:
                frequencies[character] = 1

    return frequencies


def main():
    """Run a terminal menu for Caesar cipher operations."""
    while True:
        print("\nCaesar Cipher Menu")
        print("1. Encrypt, view frequencies, and decrypt a message")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter a message: ")

            while True:
                try:
                    shift = int(input("Enter a shift value: "))
                    break
                except ValueError:
                    print("Please enter a whole number.")

            ciphered_text = caesar_cipher(message, shift)
            frequencies = letter_frequency(ciphered_text)
            deciphered_text = caesar_decipher(ciphered_text, shift)

            print("\nCiphered text:", ciphered_text)
            print("Letter frequency:")
            for letter in sorted(frequencies):
                print(letter + ":", frequencies[letter])
            print("Deciphered text:", deciphered_text)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
