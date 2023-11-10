def encryptText(rawText, key):
    start = 32
    end = 126
    range = end - start + 1

    key = (key % range + range) % range

    encryptedText = ''

    for char in rawText:

        if char == '\n':
            encryptedText += char
            continue

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

        if char == '\n':
            decryptedText += char
            continue

        charToInt = ord(char)
        shifted = charToInt - key

        if shifted < start:
            shifted += range

        decryptedChar = chr(start + (shifted - start) % range)
        decryptedText += decryptedChar

    return decryptedText


def readFromFile(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def writeToFile(filepath, text):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)

#456
while True:
    cmd = int(input("choose command: "))

    if cmd == 1:
        inputPath = input("enter input filepath: ")
        outputPath = input("enter output filepath: ")
        key = int(input("enter key: "))

        text = readFromFile(inputPath)
        encryptedText = encryptText(text, key)

        writeToFile(outputPath, encryptedText)

    if cmd == 2:
        inputPath = input("enter input filepath: ")
        outputPath = input("enter output filepath: ")
        key = int(input("enter key: "))

        text = readFromFile(inputPath)
        decryptedText = decryptText(text, key)

        writeToFile(outputPath, decryptedText)

    if cmd == 3:
        exit()