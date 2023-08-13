alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]

def get_caesar_key(newKey = 0, oldKey = 0):
    caesarKey = newKey + oldKey

    while caesarKey < 0:
        caesarKey += 26

    return caesarKey % 26 or 26

def encryptor(key = 0, message = ""):

    data = list(message)

    for index, char in enumerate(data):
        alpha = ""

        for letter in alphabet:
            if char.lower() == letter or char.upper() == letter:
                alpha = letter
        
        if alpha != "":
            alphaKey = alphabet.index(alpha) + 1
            newKey = get_caesar_key(alphaKey,key)
            newLetter = alphabet[newKey - 1]
            
            if alpha.upper() == char:
                data[index] = newLetter.upper()
            else:
                data[index] = newLetter

    return "".join(data)

encryptor(13, 'Caesar Cipher') # 'Pnrfne Pvcure')
encryptor(-5, 'Hello World!') # 'Czggj Rjmgy!')
encryptor(27, 'Whoopi Goldberg') # 'Xippqj Hpmecfsh')