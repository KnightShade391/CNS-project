def convertToBinary(text):
    textToBin = ""
    for c in text:
        textToBin += bin(ord(c))[2:].zfill(8)
    return textToBin

def convertToAscii(ciphers):
    ciphertxt = ""
    for cipher in ciphers:
        cipherIntoParts = [cipher[i:i+8] for i in range(0, len(cipher), 8)]
        for c in cipherIntoParts:
            ciphertxt += chr(int(c, 2))
    return ciphertxt