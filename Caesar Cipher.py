def caesar():
    cont = "Y"
    while cont == "Y":
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        while direction != "encode" and direction != "decode":
            direction = input(
                "Please type either 'encode' to encrypt or 'decode' to decrypt:\n").lower()

        text = input("Type your message:\n").lower()
        while checking(text) == 0:
            text = input("Please only use letters and spaces:\n").lower()
        while checking(text) == 2:
            text = input("Please don't only enter spaces:\n").lower()

        shift = int(input("Type the shift number:\n"))
        while shift < 0 or shift > 26:
            shift = int(input("Please enter a number between 0-26:\n"))

        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)
        cont = input("Y to continue the program, N to stop:\n").upper()
        while cont != "Y" and cont != "N":
            cont = input("Y to continue the program, N to stop:\n").upper()
    print("Thank you for using the Caesar Cipher!")


def encrypt(text, shift):
    newText = ""
    for char in text:
        if char.isspace():
            newText = newText + char
        else:
            newInt = ord(char) + shift
            if newInt > 122:
                newInt -= 26
            newText = newText + chr(newInt)
    print(f"The encrypted text is {newText}.")


def decrypt(text, shift):
    newText = ""
    for char in text:
        if char.isspace():
            newText = newText + char
        else:
            newInt = ord(char) - shift
            if newInt < 97:
                newInt += 26
            newText = newText + chr(newInt)
    print(f"The decrypted text is {newText}.")


def checking(text):
    if all(x.isspace() for x in text):
        return 2
    elif all(x.isalpha() or x.isspace() for x in text):
        return 1
    else:
        return 0


caesar()
