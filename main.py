def encryptText(rawText, key):
    start = 32
    end = 126
    range = end - start + 1

    key = (key % range + range) % range

    encryptedText = ''

    for char in rawText:

        charToInt = ord(char)

        encryptedChar = chr(start + (charToInt - start + key) % range)
        encryptedText += encryptedChar

    return encryptedText


def decryptText(encryptedText, key):
    start = 32
    end = 126
    range = end - start + 1

    key = (key % range + range) % range

    decryptedText = ''

    for char in encryptedText:
        charToInt = ord(char)
        shifted = charToInt - key

        if shifted < start:
            shifted += range

        decryptedChar = chr(start + (shifted - start) % range)
        decryptedText += decryptedChar

    return decryptedText


while True:
    cmd = int(input("choose command: "))

    if cmd == 1:
        text = input("input text to encrypt: ")
        key = int(input("enter key: "))

        encryptedText = encryptText(text, key)
        print(encryptedText)

    if cmd == 2:
        text = input("input text to decrypt: ")
        key = int(input("enter key: "))

        decryptedText = decryptText(text, key)
        print(decryptedText)
