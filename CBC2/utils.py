from math import floor, ceil
from random import random

# a method to split the text into equal n parts
def splitIntoParts(text, n):
    return [text[i:i+n] for i in range(0, len(text), n)]

# a method to convert the text string into binary string
def convertToBinary(text):
    textToBin = ""
    for c in text:
        textToBin += bin(ord(c))[2:].zfill(8)
    return textToBin

# a method to convert the binary string back into a text string
def convertToAscii(cipher):
    ciphertxt = ""
    cipherIntoParts = splitIntoParts(cipher, 8)
    for c in cipherIntoParts:
        ciphertxt += chr(int(c, 2))
    return ciphertxt

# a method to perform xor with zfill number of bits in the result
def xor(x, y, zfill):
    return bin(int(x, 2) ^ int(y, 2))[2:].zfill(zfill)

# method to pad extra characters to match the required length of some multiple of 16
def pad_chars(text):
    textLength = len(text)
    charsToPad = textLength % 16
    afterPad = ""
    if (text[-1] == 'x') or (text[-1] == 'X'):
        afterPad = text + ('z' * (16 - charsToPad))
    else:
        afterPad = text + ('x' * (16 - charsToPad))
    binaryStr = convertToBinary(afterPad) + bin(16 - charsToPad)[2:].zfill(128)
    return binaryStr

# a method to return two random keys
def getDESKeys():
    keys = {
        0: "mydeskey",
        1: "desmykey",
        2: "keykey11",
        3: "desdes12",
        4: "12345678",
        5: "newdesyo",
        6: "deskey12"
    }
    return [keys[floor(random() * 10) % len(keys)], keys[ceil(random() * 10) % len(keys)]]