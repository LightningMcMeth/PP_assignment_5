def encryptChar(char, key, start=32, end=126):
    if char == '\n':
        return char

    range = end - start + 1
    key = (key % range + range) % range

    return chr(start + (ord(char) - start + key) % range)


def decryptChar(char, key, start=32, end=126):
    if char == '\n':
        return char

    range = end - start + 1
    key = (key % range + range) % range

    shifted = ord(char) - key
    if shifted < start:
        shifted += range

    return chr(start + (shifted - start) % range)


def transformText(text, transformFunction, key):
    return ''.join(transformFunction(char, key) for char in text)


def readFromFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        return file.read()


def writeToFile(filePath, text):
    with open(filePath, 'w', encoding='utf-8') as file:
        file.write(text)


def processFile(inputPath, outputPath, key, transformFunction):
    text = readFromFile(inputPath)

    transformedText = transformText(text, transformFunction, key)
    writeToFile(outputPath, transformedText)


def main():
    while True:
        cmd = int(input("Choose command (1: Encrypt, 2: Decrypt, 3: Exit): "))

        if cmd in [1, 2]:
            inputPath = input("Enter input filepath: ")
            outputPath = input("Enter output filepath: ")
            key = int(input("Enter key: "))

            if cmd == 1:
                processFile(inputPath, outputPath, key, encryptChar)
            else:
                processFile(inputPath, outputPath, key, decryptChar)

        if cmd == 3:
            break


if __name__ == "__main__":
    main()
